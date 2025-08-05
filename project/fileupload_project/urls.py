from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from rest_framework.authtoken import views as drf_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('filemanager.urls')),
    path('api/token/', drf_views.obtain_auth_token),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += [
  path('', lambda request: JsonResponse({
    "message": "Welcome to the File Upload API! Use /api/upload/, /api/files/, /api/files/<filename>"
})),

]
