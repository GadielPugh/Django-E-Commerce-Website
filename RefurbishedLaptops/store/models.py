from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Laptop(models.Model):
    manufacturer = models.CharField(max_length=50)
    processor_type = models.CharField(max_length=50)
    ram_size = models.IntegerField()
    storage_type = models.CharField(max_length=20)
    storage_size = models.IntegerField()
    usb_ports = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='laptops/')
    is_sold = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default="Unnamed Laptop")
    description = models.TextField(default="No description available")

    def __str__(self):
        return f"{self.name} by {self.manufacturer}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.TextField()
    bank_account_name = models.CharField(max_length=100)
    bank_account_number = models.CharField(max_length=20)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100, default="Anonymous Buyer")
    address = models.TextField(default="No address provided")
    bank_account_name = models.CharField(max_length=100, default="No Account Name Provided")  # New field
    bank_account_number = models.CharField(max_length=20, default="000000000")
    date_of_purchase = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
