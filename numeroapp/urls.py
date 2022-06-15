# importations
from django.conf import settings
from django.urls import path
from django import views
from . import views
from django.conf.urls.static import static

# urls paths
urlpatterns = [
    path('', views.index, name='index'),
    path('newProject', views.add_project, name='new_project'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
