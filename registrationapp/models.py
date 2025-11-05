from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields :
    phone = models.CharField(max_length=15)
    door_no = models.CharField(max_length=5)
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    userpic = models.ImageField(upload_to='userpics/',blank=True, null=True)