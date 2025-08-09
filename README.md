# Django File Upload API

A secure Django REST API to upload, list, and download files with token-based authentication, file type/size validation, and media file handling.

---

##  Features

- 🔒 Token Authentication
- 📁 File Upload with size/type validation
- 📝 File List API
- 📥 File Download API
- 🔐 Only authenticated users can access/upload/download
- 🧾 Allowed types: `.png`, `.jpg`, `.jpeg`, `.pdf`
- 🚫 Max size: 5 MB

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

## 📮 API Endpoints

### 🔑 Get Auth Token

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

### 📤 Upload File

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

### 📥 Download File

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

## 🧪 Testing in Postman

1. **Login with `/api/token/`** to get token
2. **Set Authorization Header:**
   ```
   Authorization: Token <your_token>
   ```
3. **Use the above routes to Upload/List/Download files**

---

## 📂 Media Settings

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'
```
## Project Demo

<img width="1387" height="855" alt="1" src="https://github.com/user-attachments/assets/0231a98e-f050-46d9-b166-e2c7212cd428" />
<img width="1887" height="976" alt="2" src="https://github.com/user-attachments/assets/40d71eb0-298d-4a80-a523-6813836f0b58" />
<img width="1378" height="693" alt="3" src="https://github.com/user-attachments/assets/9055fbc4-41c1-420c-ae7c-888dcd43e4b4" />
<img width="1386" height="870" alt="4" src="https://github.com/user-attachments/assets/a31786ab-ed04-4bde-80fd-fadac1a0aa9b" />
<img width="1771" height="867" alt="5" src="https://github.com/user-attachments/assets/47427aa6-021e-4e13-8ce2-f816dce80b56" />

