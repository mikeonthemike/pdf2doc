# PDF to DOCX Converter Web Application

This project is a simple web application built with Flask that allows users to upload a PDF file and convert it to a DOCX file. The converted file is then available for download directly through the web interface.

## Features

- **Upload PDF Files**: Users can upload a PDF file from their local system.
- **Convert to DOCX**: The application converts the uploaded PDF file into a DOCX format.
- **Download Converted File**: The converted DOCX file is available for download.

## Project Structure

```
pdf_converter_app/
│
├── main.py                 # Main application script
├── templates/
│   ├── index.html         # HTML template for the upload form
├── static/
│   ├── styles.css         # Optional CSS for styling
│
├── uploads/               # Directory to store uploaded PDF files
├── outputs/               # Directory to store converted DOCX files
└── requirements.txt       # Python package dependencies
```

## Prerequisites

- **Python 3.x**: Make sure you have Python 3.x installed on your machine.
- **pip**: Python package manager for installing dependencies.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/pdf-to-docx-converter.git
   cd pdf-to-docx-converter
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Access the Web Interface**:

   Open your browser and go to `http://127.0.0.1:5000/`.

3. **Upload and Convert**:

   - Upload a PDF file using the provided form.
   - Click the "Convert" button.
   - The converted DOCX file will be available for download.

## Project Dependencies

- **Flask**: A lightweight WSGI web application framework.
- **Flask-Testing**: an extension for testing Flask applications.
- **pdf2docx**: A Python library for converting PDF files to DOCX format.

These dependencies are listed in the `requirements.txt` file.

## Directory Structure

- **`main.py`**: The main Flask application file that handles routes, file uploads, and conversion logic.
- **`templates/index.html`**: The HTML template for the web interface.
- **`static/styles.css`**: The CSS file for styling the web interface.
- **`uploads/`**: Directory where uploaded PDF files are stored.
- **`outputs/`**: Directory where converted DOCX files are stored.

## Customization

You can customize the application by modifying the HTML template (`templates/index.html`), adding more features to the Flask routes in `app.py`, or enhancing the CSS styles in `static/styles.css`.

## Testing
Run:
   ```bash
   python -m unittest discover -s tests
   ```

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please open an issue on this repository.
