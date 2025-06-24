from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def signin(request):
    if request.method == 'POST':

        #Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        #TODO
        #Check if the user exists
        user = authenticate(request, username=username, password=password)
        breakpoint()
        #If the user exists, log in and redirect to the dashboard
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials, please register first.')
            return redirect('signup')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        #Check if the user or the email already exists 
        username_exists = User.objects.filter(username=username).exists()
        email_exists = User.objects.filter(email=email).exists()

        #The password is hashed to avoid leaking information
        password_hashed = make_password(password)
        
        if username_exists or email_exists:
            messages.error(request, 'Username or email already exists. Please enter a different one.')
            return redirect('signup')
        else:
            try:
                if password == repeat_password:
                    User.objects.create(
                        username=username,
                        password=password_hashed,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                    )
                    messages.success(request, 'The user has been created successfully.')
                    return redirect('dashboard')
            except:
                messages.error(request, 'Passwords do not match. Please enter the same password.')
                return redirect('signup')

    return render(request,'signup.html')

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        messages.error(request, 'You must be logged in to access the admin dashboard.')
        return render(request, 'dashboard.html')

def prueba_mensaje(request):
    messages.success(request, "Este es un mensaje de prueba")
    return redirect('/')  # o cualquier vista válida