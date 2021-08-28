from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# from django.db import models
# from master.Models.dealership import Dealership


action = (('Male', 'Male'),
          ('Female', 'Female'))


class CustomUser(AbstractUser):
    Address = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100, null=True)
    Date_Of_Birth = models.DateField(auto_now_add=False, null=True)
    Gender = models.CharField(max_length=50, choices=action, null=True)
    Occupation = models.CharField(max_length=100, null=True)
    objective = models.CharField(max_length=100, null=True)
    Age = models.IntegerField(null=True)
    Country = models.CharField(max_length=50,null=True)
    PostalCode = models.IntegerField(null=True)
    AboutMe = models.TextField(max_length=10000,null=True)
    # Connect_Payment = models.BooleanField(null=True)

    class Meta:
        db_table = 'auth_user'


# class PaymentModel(models.Model):
#     User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     Card_Name = models.CharField(max_length=100)
#     Card_Number = models.PositiveIntegerField()
#     Expiry_Date = models.DateField()


class BillingAddress(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Address_line_1 = models.CharField(max_length=250)
    Address_line_2 = models.CharField(max_length=250)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip_Code = models.IntegerField()
    Country = models.CharField(max_length=100)
