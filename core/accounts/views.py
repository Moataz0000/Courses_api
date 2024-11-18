from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate






def sign_up(request):
    
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('courses:subject_courses_list')

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