import os
from django.test import TestCase, Client
from .utils import handle_uploaded_file
from django.conf import settings
from bs4 import BeautifulSoup

# Create your tests here.

def upload_file(filename, client):
    upload_path = os.path.join(settings.BASE_DIR, filename)
    with open(upload_path, 'rb') as attachment:
        response = client.post('/', {'cv':attachment},format='multipart')
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    return None

class Upload(TestCase):
    """
        Mimics upload scenario as uploaded form UI
        1. Proper CV in doc format
        2. Proper CV in docx format
        3. Proper CV in pdf format
        4. File with a wrong format
        5. File with right extension but no data
    """
    def setUp(self):
        self.client = Client()

    def test_doc_with_skills(self):
        """
            CV in doc format is properly parsed and skills are extracted
        """
        skills = []
        soup = upload_file("tests/test1.doc", self.client)
        skills = soup.find_all("span", class_="badge badge-primary")
        self.assertNotEqual(0, len(skills))

    def test_docx_with_skills(self):
        """
            CV in docx format is properly parsed and skills are extracted
        """
        skills = []
        soup = upload_file("tests/test2.docx", self.client)
        skills = soup.find_all("span", class_="badge badge-primary")
        self.assertNotEqual(0, len(skills))

    def test_pdf_with_skills(self):
        """
            CV in pdf format is properly parsed and skills are extracted
        """
        skills = []
        soup = upload_file("tests/test3.pdf", self.client)
        skills = soup.find_all("span", class_="badge badge-primary")
        self.assertNotEqual(0, len(skills))

    def test_wrong_extension_files(self):
        """
            Proper error message is thrown for file with wrong extension
        """
        soup = upload_file("tests/test4.txt", self.client)
        message = soup.find("div", class_="invalid-form-message").contents[0]
        self.assertEqual("Error processing your CV. Please reupload it", message)

    def test_right_extension_files_no_content(self):
        """
            Proper error message is thrown for file with right extension
            and from which skills cannot be extracted.
        """
        soup = upload_file("tests/test5.doc", self.client)
        message = soup.find("div", class_="invalid-form-message").contents[0]
        self.assertEqual("Cannot extract skills form your CV.", message)