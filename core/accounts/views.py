from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate
from .models import InstructorProfile
from .forms import InstructorProfileForm
from django.contrib.auth.decorators import login_required



def sign_up(request):
    
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            InstructorProfile.objects.create(user=user)
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:view-profile')

    context = {
        'form':form
    }
    return render(request, 'accounts/sign_up.html', context)




def sign_in(request):
    ERROR = None
    if request.user.is_authenticated:
        return redirect('courses:subject_courses_list')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('courses:subject_courses_list')
        else:
            ERROR = 'Invalid credentials!, Password or username is invalid!'
    
    
    context = {
        'error':ERROR
    }        
    
    return render(request, 'accounts/sing_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('accounts:sign_up')



@login_required(login_url='accounts:sign_up')
def edit_profile(requset):
    profile = get_object_or_404(InstructorProfile, user=requset.user)
    form    = InstructorProfileForm(instance=profile)
    if requset.method == 'POST':
        form = InstructorProfileForm(requset.POST, requset.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:view-profile')
    
    context = {
        'form':form,
    }    
    
    return render(requset, 'accounts/edit_profile.html', context)


@login_required(login_url='accounts:sign_up')
def view_profile(request):
    profile = get_object_or_404(InstructorProfile, user=request.user)
    context = {
        'profile':profile
    }
    return render(request, 'accounts/view_profile.html', context)