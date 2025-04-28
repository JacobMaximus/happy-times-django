from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def menu(request):
    return render(request, 'home/pages/menu.html')

def cart(request):
    return render(request, 'home/pages/cart.html')
