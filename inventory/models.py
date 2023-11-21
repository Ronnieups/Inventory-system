from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

class Supplier(models.Model):
    name = models.CharField(max_length=255)

    

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('user', 'User')])

class Sale(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'Sale #{self.pk} - ${self.amount}'