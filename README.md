# Django Resume Uploader

A simple web application built with Django to upload, store, and view candidate resumes.

## 🔍 Features

- Upload resumes via admin interface or form (optional).
- View candidate details (name, email, resume).
- Download resumes directly.
- Uses Django's built-in file storage and SQLite database.

---

## 🛠 Tech Stack

- Python 3.13+
- Django 5.x
- SQLite (default)
- HTML/CSS (basic frontend)

---
Project Structure
DjangoResumeUploader/
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       ├── home.html
│   │       └── detail.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── resumeuploader/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md

Future Enhancements
Add a user-facing resume upload form

Search/filter candidates

Use PostgreSQL for production

Add file type/size validation

Resume preview (PDF rendering)
