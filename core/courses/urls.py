from django.urls import path
from . import views



app_name = 'courses'


urlpatterns = [
    path('', views.subject_courses_list, name='subject_courses_list'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('add-course/', views.add_course, name='add_course'),

]