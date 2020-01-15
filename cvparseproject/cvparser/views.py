import time
from .utils import handle_uploaded_file
from django.shortcuts import render
from django.views.generic import View
from .forms import CVForm

# Create your views here.


class UploadView(View):
    def get(self, request):
        context = {"form": CVForm()}
        return render(request, "fileupload.html", context)

    def post(self, request):
        form = CVForm(request.POST or None, request.FILES or None)
        context = {"form": form}
        cvfile = request.FILES.get("cv", None)
        if cvfile and cvfile.name.split(".")[-1].lower() in ["pdf", "doc", "docx"]:
            start_time = time.time()
            skills = handle_uploaded_file(cvfile)
            end_time = time.time()
            context.update(
                {"skills": skills, "process_time": end_time - start_time}
            )
            if not skills:
                context.update({"message": "Cannot Extract skills form your CV."})
        else:
            context.update({"message": "Error processing your CV. Please reupload it"})
        return render(request, "fileupload.html", context)
