from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return render(request, 'dashboard_admin.html')
        else:
            messages.error(request, 'Invalid credentials, please register first.')
            return redirect(request, 'signup.html')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # # Create a new user
        # user = User.objects.create_user(username=username, password=password)
        # user.save()

    return render(request,'signup.html')

def index(request):
    return render(request, 'index.html')

def dashboard_admin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard_admin.html')
    else:
        messages.error(request, 'You must be logged in to access the admin dashboard.')
        return render(request, 'signin.html')