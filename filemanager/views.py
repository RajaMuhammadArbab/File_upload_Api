import os
import uuid
from django.conf import settings
from django.http import FileResponse
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from django.utils.text import get_valid_filename

ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.pdf']
MAX_SIZE = 5 * 1024 * 1024  

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def upload_file(request):
    uploaded_file = request.FILES.get('file')
    if not uploaded_file:
        return Response({"error": "No file provided."}, status=400)

    ext = os.path.splitext(uploaded_file.name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return Response({"error": "File type not allowed."}, status=400)

    if uploaded_file.size > MAX_SIZE:
        return Response({"error": "File size exceeds 5MB limit."}, status=400)

 
    safe_name = get_valid_filename(uploaded_file.name)
    unique_prefix = uuid.uuid4().hex
    final_name = f"{unique_prefix}_{safe_name}"

   
    save_path = os.path.join(settings.MEDIA_ROOT, final_name)
    with open(save_path, 'wb+') as dest:
        for chunk in uploaded_file.chunks():
            dest.write(chunk)

    
    file_record = UploadedFile.objects.create(
        name=final_name,
        file=final_name,
        size=uploaded_file.size
    )

    serializer = UploadedFileSerializer(file_record)
    return Response(serializer.data, status=201)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def list_files(request):
    files = UploadedFile.objects.all()
    serializer = UploadedFileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def download_file(request, filename):
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    if not os.path.exists(filepath):
        return Response({"error": "File not found."}, status=404)
    return FileResponse(open(filepath, 'rb'), as_attachment=True)
