from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import InventoryItem
from .forms import CategoryForm, SupplierForm, InventoryItemForm

def home(request):
    return render(request, 'inventory/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'inventory/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def input_data(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_data')
    else:
        form = InventoryItemForm()

    return render(request, 'inventory/input_data.html', {'form': form})

@login_required
def retrieve_data(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/retrieve_data.html', {'items': items})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()

    return render(request, 'inventory/add_category.html', {'form': form})

@login_required
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_supplier')
    else:
        form = SupplierForm()

    return render(request, 'inventory/add_supplier.html', {'form': form})
