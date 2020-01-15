import os
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from .forms import CVForm
from pyresparser import ResumeParser

# Create your views here.


class UploadView(View):
    def get(self, request):
        context = {"form": CVForm(), "skills": None}
        return render(request, "fileupload.html", context)

    def post(self, request):
        data = None
        form = CVForm(request.POST or None, request.FILES or None)
        context = {"form": form}
        cvfile = request.FILES.get("cv")
        if cvfile.name.split(".")[-1].lower() in ["pdf", "doc"]:
            data = handle_uploaded_file(cvfile)
        if data:
            context.update({"skills": data})
        return render(request, "fileupload.html", context)


def handle_uploaded_file(cv):
    upload_path = os.path.join(settings.BASE_DIR, "uploads", cv.name)
    print(upload_path)
    with open(upload_path, "wb+") as destination:
        for chunk in cv.chunks():
            destination.write(chunk)
    data = ResumeParser(upload_path).get_extracted_data()
    os.remove(upload_path)
    print(data)
    return data
