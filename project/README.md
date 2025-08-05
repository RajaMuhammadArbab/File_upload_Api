# Django File Upload API

A secure Django REST API to upload, list, and download files with token-based authentication, file type/size validation, and media file handling.

---

##  Features

-  Token Authentication
-  File Upload with size/type validation
-  File List API
-  File Download API
-  Only authenticated users can access/upload/download
-  Allowed types: `.png`, `.jpg`, `.jpeg`, `.pdf`
- Max size: 5 MB

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone <your_repo_url>
cd fileupload_project
```

### 2. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (for testing/admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

---

##  File: `requirements.txt`

```
Django>=3.2
djangorestframework
```

---

##  Project Structure

```
fileupload_project/
├── filemanager/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── fileupload_project/
│   ├── settings.py
│   └── urls.py
├── uploads/             
├── manage.py
└── requirements.txt
```

---

##  API Endpoints

###  Get Auth Token

**POST** `/api/token/`

**Body (form-data or JSON):**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

> Returns:
```json
{"token": "<your_token>"}
```

---

###  Upload File

**POST** `/api/upload/`

**Headers:**
```
Authorization: Token <your_token>
```

**Body (form-data):**
```
file: <your_file>
```

---

### 📄 List Uploaded Files

**GET** `/api/files/`

**Headers:**
```
Authorization: Token <your_token>
```

> Returns:
```json
[
  {
    "id": 1,
    "name": "b85a3c4aa8_Resume.pdf",
    "file": "/media/b85a3c4aa8_Resume.pdf",
    "size": 99959,
    "uploaded_at": "2025-08-05T08:22:39.900513Z"
  },
  ...
]
```

---

###  Download File

**GET** `/api/files/<filename>/`

**Headers:**
```
Authorization: Token <your_token>
```

**Example:**
```
/api/files/b85a3c4aa8_Resume.pdf/
```

---

##  Testing in Postman

1. **Login with `/api/token/`** to get token
2. **Set Authorization Header:**
   ```
   Authorization: Token <your_token>
   ```
3. **Use the above routes to Upload/List/Download files**

---

##  Media Settings

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'
```
