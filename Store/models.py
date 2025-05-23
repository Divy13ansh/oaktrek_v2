from django.db import models
from Profile.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Skincare', 'Skincare'),
        ('Haircare', 'Haircare'),
        ('Bodycare', 'Bodycare'),
        # Add more if needed
    ]

    GENDER_CHOICES = [
        ('Unisex', 'Unisex'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    price = models.FloatField()
    rating = models.FloatField(default=0.0)
    image_1 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.product_name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.product_name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.product_name} x {self.quantity}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wishlist item: {self.product.product_name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey('Profile.Address', on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    