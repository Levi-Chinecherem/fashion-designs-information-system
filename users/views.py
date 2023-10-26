# users/views.py

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Determine the user's group choice
            group_name = request.POST.get('group')  # You need to add this field to your form
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            # Log the user in after registration
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        # Process login form data
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to a user-specific page
        else:
            # Handle login failure
            pass
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    # Your dashboard logic can go here
    # For example, you can retrieve user-specific data to display on the dashboard
    context = {
        'username': request.user.username,  # Replace with your user data
        'fashion_items': ['Item 1', 'Item 2', 'Item 3'],  # Sample fashion items
    }
    return render(request, 'dashboard.html', context)
