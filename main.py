from flask import Flask, render_template, request, send_file, redirect, url_for
from pdf2docx import Converter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload and output folders
UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'outputs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        file = request.files['pdf_file']
        if file:
            filename = secure_filename(file.filename)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(pdf_path)

            # Convert PDF to DOCX
            docx_filename = os.path.splitext(filename)[0] + '.docx'
            docx_path = os.path.join(app.config['OUTPUT_FOLDER'], docx_filename)
            convert_pdf_to_docx(pdf_path, docx_path)

            return send_file(docx_path, as_attachment=True)

    return render_template('index.html')

def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

if __name__ == '__main__':
    app.run(debug=True)
