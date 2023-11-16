from django import forms
from .models import Category, Supplier, InventoryItem

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name']

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'price', 'category', 'supplier']