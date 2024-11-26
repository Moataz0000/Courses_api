from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, Course
from django.contrib.auth.decorators import login_required
from .forms import CourseForm



def subject_courses_list(request):
    subjects = Subject.objects.prefetch_related('courses').all()
    return render(request, 'course/subject_course_list.html', context={'subjects':subjects})



def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'detail':course,
    }
    return render(request, 'course/course_detail.html', context)




@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user
            course.save()
            return redirect('courses:subject_courses_list')
    else:
        form = CourseForm()    
    
    context = {
        'form':form
    }
    
    return render(request, 'course/add_course.html', context)




@login_required
def edit_course(request, slug):
    course = get_object_or_404(Course, slug=slug, owner=request.user)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save() 
            return redirect('accounts:view-profile')

    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'course/edit_coures.html', context)