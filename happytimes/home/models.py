from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    def __str__(self):
        return self.email



# from django.db import models

# class User(models.Model):
#     id = models.AutoField(primary_key=True)  # Will auto-increment
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.email


# class Admin(models.Model):
#     id = models.AutoField(primary_key=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.email

# class Cake(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100) 
#     description = models.TextField()
#     price_per_gram = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self):
#         return self.name


# class OrderList(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50, default="pending")  # e.g., pending, in progress, done

#     def __str__(self):
#         return f"Order #{self.id} by {self.user.email}"


# class OrderDetail(models.Model):
#     order = models.ForeignKey(OrderList, on_delete=models.CASCADE)
#     cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)

#     class Meta:
#         unique_together = (("order", "cake"),)

#     def __str__(self):
#         return f"{self.cake.name} in Order #{self.order.id}"
