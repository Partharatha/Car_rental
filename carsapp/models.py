from django.db import models


# Create your models here.

time_slot=[
        ('9:00-10:00','9:00-10:00'),
        ('10:00-11:00','10:00-11:00'),
        ('11:00-12:00','11:00-12:00'),
        ('12:00-13:00','12:00-13:00'),
        ('13:00-14:00','13:00-14:00'),
        ('14:00-15:00','14:00-15:00'),
        ('15:00-16:00','15:00-16:00'),
        ('16:00-17:00','16:00-17:00'),
    ]
class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    est_year = models.IntegerField()
    origin = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos',blank=True,null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    seat_capacity = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    cc = models.CharField(max_length=100)
    miliege = models.CharField(max_length=100)
    pro_img = models.ImageField(upload_to='car_img',blank=True,null=True)
    price = models.IntegerField()

class ProductInteriorImgs(models.Model):
    interior = models.ImageField(upload_to='product_img/interior_img', blank=True, null=True)
    product = models.ForeignKey(Products, related_name='interior_images', on_delete=models.CASCADE)

class ProductExteriorImgs(models.Model):
    exterior = models.ImageField(upload_to='product_img/exterior_img', blank=True, null=True)
    product = models.ForeignKey(Products, related_name='exterior_images', on_delete=models.CASCADE)     


class Bookdrive(models.Model):
    product_name=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    timings=models.CharField(max_length=100,choices=time_slot)
   
def __str__(self):
        return self.user.username

class Enquiry(models.Model):
    user_name=models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    consern = models.TextField()

    def __str__(self):
         return f"Enquiry from {self.user.username if self.user else self.phone}"