from django.shortcuts import render, get_object_or_404
from .models import Cake, OrderList, OrderDetail, User

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def menu(request):
    return render(request, 'home/pages/menu.html')

def cart(request):
    return render(request, 'home/pages/cart.html')

def login(request):
    return render(request, 'home/loginAndAdmin/user-login.html')

def admin(request):
    return render(request, 'home/loginAndAdmin/admin-login.html')

def admin_panel(request):
    return render(request, 'home/loginAndAdmin/admin-panel.html')

# # Show all cakes (for the menu page)
# def menu_view(request):
#     cakes = Cake.objects.all()
#     return render(request, 'home/pages/menu.html', {'cakes': cakes})

# # Display order summary

# def order_summary(request, order_id):
#     order = get_object_or_404(OrderList, pk=order_id)
#     details = OrderDetail.objects.filter(order=order)
#     return render(request, 'home/pages/order_summary.html', {'order': order, 'details': details})
