from django.shortcuts import render
from .models import Subject
# Create your views here.




def subject_courses_list(request):
    subjects = Subject.objects.prefetch_related('courses').all()
    return render(request, 'course/subject_course_list.html', context={'subjects':subjects})