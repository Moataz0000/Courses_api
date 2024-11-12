from django.urls import path
from . import views



app_name = 'courses'


urlpatterns = [
    path('', views.subject_courses_list, name='subject_courses_list')
]