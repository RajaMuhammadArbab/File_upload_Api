from django.urls import path
from .views import upload_file, list_files, download_file

urlpatterns = [
    path('upload/', upload_file, name='upload-file'),
    path('files/', list_files, name='list-files'),
    path('files/<str:filename>', download_file, name='download-file'),
]
