import time
from .utils import handle_uploaded_file
from django.shortcuts import render
from django.views.generic import View
from .forms import CVForm

# Create your views here.


class UploadView(View):
    def get(self, request):
        context = {"form": CVForm(), "skills": None, "process_time": None}
        return render(request, "fileupload.html", context)

    def post(self, request):
        data = None
        form = CVForm(request.POST or None, request.FILES or None)
        context = {"form": form}
        cvfile = request.FILES.get("cv")
        if cvfile.name.split(".")[-1].lower() in ["pdf", "doc"]:
            start_time = time.time()
            data = handle_uploaded_file(cvfile)
            end_time = time.time()
            context.update({"skills": data.get("skills"), "process_time": end_time - start_time})
        return render(request, "fileupload.html", context)
