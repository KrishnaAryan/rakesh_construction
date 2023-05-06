
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('general_construction', views.general_construction, name='general_construction'),
    path('property_maintenance', views.property_maintenance, name='property_maintenance'),
    path('project_managment', views.project_managment, name='project_managment'),
    path('virtual_design_build', views.virtual_design_build, name='virtual_design_build'),
    path('preconstruction', views.preconstruction, name='preconstruction'),
    path('design_build', views.design_build, name='design_build'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('projects_single/<int:pk>', views.projects_single, name='projects_single'),
    path('team_single', views.design_build, name='team_single'),
    path('success_page', views.success_page, name='success_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    