from django.shortcuts import render,redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'home/index.html', {'user': request.user})

def menu(request):
    return render(request, 'home/pages/menu.html', {'user': request.user})

def cart(request):
    return render(request, 'home/pages/cart.html', {'user': request.user})

#logout
def logout_view(request):
    logout(request)
    return redirect('/')


# def login(request):
#     return render(request, 'home/loginAndAdmin/user-login.html')

# def admin(request):
#     return render(request, 'home/loginAndAdmin/admin-login.html')

# def admin_panel(request):
#     return render(request, 'home/loginAndAdmin/admin-panel.html')

''''''
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.hashers import make_password
from .models import CustomUser

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone_number')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            return JsonResponse({'success': False, 'error': 'Passwords do not match'})

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'error': 'Email already registered'})

        if CustomUser.objects.filter(phone_number=phone).exists():
            return JsonResponse({'success': False, 'error': 'Phone number already registered'})

        CustomUser.objects.create(
            username=email,
            name=name,
            email=email,
            phone_number=phone,
            password=make_password(password)
        )
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password)
        if request.user.is_authenticated:
            # Logged in
            name = request.user.password
            email = request.user.email
            # print(name, email)

        if user is not None:
            django_login(request, user) # creating login sessions.
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def user_login_page(request):
    return render(request, 'home/userLogin/user-login.html')

#user profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')  # redirects to login page if not logged in
def profile_view(request):
    return render(request, 'home/userLogin/profile.html', {'user': request.user})
