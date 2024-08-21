import unittest
import os
from main import app

class PDFToDOCXConverterTestCase(unittest.TestCase):

    def setUp(self):
        # Configure the Flask app to be in testing mode
        app.config['TESTING'] = True
        app.config['UPLOAD_FOLDER'] = 'tests/test_uploads/'
        app.config['OUTPUT_FOLDER'] = 'tests/test_outputs/'
        self.app = app.test_client()

        # Ensure test directories exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

    def tearDown(self):
        # Clean up after each test
        for folder in [app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER']]:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.unlink(file_path)

    def test_homepage_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Convert PDF to DOCX', response.data)

    def test_pdf_upload_and_conversion(self):
        # Test file path
        test_pdf_path = 'tests/test_files/sample.pdf'

        # Upload the PDF and convert it
        with open(test_pdf_path, 'rb') as test_pdf:
            response = self.app.post('/', data={
                'pdf_file': test_pdf
            }, content_type='multipart/form-data')

        # Check that the response is a file download
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/vnd.openxmlformats-officedocument.wordprocessingml.document', response.content_type)

        # Check that the output file exists
        output_files = os.listdir(app.config['OUTPUT_FOLDER'])
        self.assertEqual(len(output_files), 1)
        self.assertTrue(output_files[0].endswith('.docx'))

if __name__ == '__main__':
    unittest.main()
