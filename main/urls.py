from django.urls import path
from . views import index, clientComments
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('comments/', clientComments, name='clientcomments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
