from django.shortcuts import render, get_object_or_404
# from .models import Cake, OrderList, OrderDetail, User

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {'user': request.user})

def menu(request):
    return render(request, 'home/pages/menu.html', {'user': request.user})

def cart(request):
    return render(request, 'home/pages/cart.html', {'user': request.user})


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

#logout
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')



# # Show all cakes (for the menu page)
# def menu_view(request):
#     cakes = Cake.objects.all()
#     return render(request, 'home/pages/menu.html', {'cakes': cakes})

# # Display order summary

# def order_summary(request, order_id):
#     order = get_object_or_404(OrderList, pk=order_id)
#     details = OrderDetail.objects.filter(order=order)
#     return render(request, 'home/pages/order_summary.html', {'order': order, 'details': details})

# ''''''
# import json
# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from django.contrib.auth.hashers import make_password, check_password
# from .models import User

# @require_http_methods(["POST"])
# def signup(request):
#     try:
#         data = json.loads(request.body)
#         email = data.get('email')
#         phone_number = data.get('phone')
#         password = data.get('password')
        
#         if not all([email, phone_number, password]):
#             return JsonResponse({
#                 'success': False,
#                 'errors': {'general': 'All fields are required'}
#             }, status=400)

#         # Check if user already exists
#         if User.objects.filter(email=email).exists():
#             return JsonResponse({
#                 'success': False,
#                 'errors': {'email': 'Email already registered'}
#             }, status=400)
        
#         if User.objects.filter(phone_number=phone_number).exists():
#             return JsonResponse({
#                 'success': False,
#                 'errors': {'phone': 'Phone number already registered'}
#             }, status=400)

#         # Create new user
#         user = User.objects.create(
#             email=email,
#             phone_number=phone_number,
#             password=make_password(password)
#         )

#         return JsonResponse({'success': True})

#     except json.JSONDecodeError:
#         return JsonResponse({
#             'success': False,
#             'errors': {'general': 'Invalid JSON data'}
#         }, status=400)
#     except Exception as e:
#         return JsonResponse({
#             'success': False,
#             'errors': {'general': str(e)}
#         }, status=500)

# @require_http_methods(["POST"])
# def user_login(request):
#     try:
#         data = json.loads(request.body)
#         email = data.get('email')
#         password = data.get('password')

#         if not all([email, password]):
#             return JsonResponse({
#                 'success': False,
#                 'errors': {'general': 'Email and password are required'}
#             }, status=400)

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return JsonResponse({
#                 'success': False,
#                 'errors': {'general': 'Invalid credentials'}
#             }, status=401)

#         if not check_password(password, user.password):
#             return JsonResponse({
#                 'success': False,
#                 'errors': {'general': 'Invalid credentials'}
#             }, status=401)

#         # Set session data
#         request.session['user_id'] = user.id
#         request.session['email'] = user.email

#         return JsonResponse({'success': True})

#     except json.JSONDecodeError:
#         return JsonResponse({
#             'success': False,
#             'errors': {'general': 'Invalid JSON data'}
#         }, status=400)
#     except Exception as e:
#         return JsonResponse({
#             'success': False,
#             'errors': {'general': str(e)}
#         }, status=500)