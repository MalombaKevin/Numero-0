# importations
from django.conf import settings
from django.urls import path
from django import views
from . import views
from django.conf.urls.static import static

# urls paths
urlpatterns = [
    path('', views.index, name='index'),
    path('newProject/', views.add_project, name='new_project'),
    path('newProfile/', views.add_profile, name='new_profile'),
    path('profile/', views.profile, name='profile'),
    path('project/<int:id>/', views.project_details, name='details'),
    path('numerologers/',views.numerologers, name='users'),
    path('numerologers/user/<int:id>',views.numerologer, name='numerologer'),
    path('search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
