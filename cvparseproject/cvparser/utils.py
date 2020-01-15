import os
import en_core_web_sm

from django.conf import settings
from pyresparser import ResumeParser

nlp = en_core_web_sm.load()


def handle_uploaded_file(cv):
    """
        Extracts skills mentioned in a CV.

        Saves uploaded CV in a temporary location and uses
        pyresparser to extract all necessary informatiion from
        that CV. After extraction, Uploaded file is deleted.

        Parameters:
        cv (file): CV uploaded form UI

        Returns:
        list of string: List of skills extracted from CV. Might be empty list
                        if it is unable to extract skills
    """
    upload_path = os.path.join(settings.BASE_DIR, "uploads", cv.name)
    with open(upload_path, "wb+") as destination:
        for chunk in cv.chunks():
            destination.write(chunk)
    try:
        data = ResumeParser(upload_path).get_extracted_data()
    except Exception:
        data = {"skills": []}
    finally:
        os.remove(upload_path)
    return data.get("skills", [])
