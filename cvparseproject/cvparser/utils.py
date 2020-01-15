import os
from django.conf import settings
from pyresparser import ResumeParser


def handle_uploaded_file(cv):
    upload_path = os.path.join(settings.BASE_DIR, "uploads", cv.name)
    with open(upload_path, "wb+") as destination:
        for chunk in cv.chunks():
            destination.write(chunk)
    data = ResumeParser(upload_path).get_extracted_data()
    os.remove(upload_path)
    return data
