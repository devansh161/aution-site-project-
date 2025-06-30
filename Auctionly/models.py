from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField()
    mobile = models.BigIntegerField(unique=True)
    text = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    starting_bid = models.DecimalField(max_digits=20, decimal_places=2)
    end_auction = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='buyer')
    notified = models.BooleanField(default=False)
    is_auction_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.user} - {self.amount}"
    