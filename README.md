# CV Parser

```
A webapp that parses resume in DOC/DOCX/PDF format and extracts information regarding skillsets mentioned in that resume.
```

Built by  [Aakash Shrestha](https://github.com/aakashres)

---
# Installation
This project is based on Django==3.0.2 and a library named [pyresparser](https://pypi.org/project/pyresparser/). You can run this site using following commands.

```bash
git clone https://github.com/aakashres/cvparser.git
cd cvparser
pip install -r requirements.txt
python -m nltk.downloader words
cd cvparseproject
python manage.py runserver
```

# Supported File Formats

- PDF and DOCx files are supported on all Operating Systems
- If you want to extract DOC files you can install [textract](https://textract.readthedocs.io/en/stable/installation.html) for your OS (Linux, MacOS)
- Note: You just have to install textract (and nothing else) and doc files will get parsed easily