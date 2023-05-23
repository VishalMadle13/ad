from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print("111111111111111111")
        for f in form :
            print(f)
        if form.is_valid():
            print("22222222222222")
            user = form.save(commit=False)
            user.role = 'applicant'  # Assign the role as "applicant" by default
            print("33333333333333")
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'administrator':
                return redirect('admin_dashboard')
            else:
                return redirect('applicant_dashboard')
        else:
            return redirect('login')
    return render(request, 'login.html')

@user_passes_test(lambda u: u.role == 'administrator')
@login_required
def admin_dashboard(request):
    # Implement admin dashboard logic here
    return render(request, 'admin_dashboard.html')

@login_required
def applicant_dashboard(request):
    # Implement applicant dashboard logic here
    return render(request, 'applicant_dashboard.html')
