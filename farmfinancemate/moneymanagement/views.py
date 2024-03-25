from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

# base page for the app
def base(request):
    """
    This function renders the base page

    Args:
        request: request object

    Returns:
        render: renders the base page
    """
    return render(request, 'base.html')

# register page for user registration
def register_page(request):
    """
    This function registers a user

    Args:
        request: request object

    Returns:
        render: renders the register page if the request method is GET, else redirects to login page
    """
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exists')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    messages.success(request, 'User created successfully')
                    return redirect('login')
            except Exception as e:
                messages.info(request, 'Error creating user')
                return redirect('register')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

# login page for user login
def login_page(request):
    """
    This function logs in a user

    Args:
        request: request object

    Returns:
        render: renders the login page if the request method is GET, else redirects to home page
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('login')
        except Exception as e:
            messages.info(request, 'Error logging in')
            return redirect('login')
    return render(request, 'login.html')

# logout view
@login_required
def logout_page(request):
    """
    This function logs out a user

    Args:
        request: request object

    Returns:
        redirect: redirects to home page
    """
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/')
