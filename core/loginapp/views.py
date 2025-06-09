from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
            messages.error(request, 'Invalid credentials')
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def index(request):
    return render(request, 'index.html')

def dashboard_admin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard_admin.html')
    else:
        messages.error(request, 'You must be logged in to access the admin dashboard.')
        return render(request, 'signin.html')