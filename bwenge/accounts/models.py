from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManger

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255, unique=True,verbose_name="Email Address")
    first_name= models. CharField(max_length=100, verbose_name=_("First Name"))
    last_name= models.CharField(max_length=100, verbose_name=_("Last Name"))
    is_staff=models. BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active=models. BooleanField(default=True)
    date_joined = models. DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD="email"

    REQUIRED_FIELDS= ["first_name", "last_name"]

    objects= UserManger()
    
    def __str__(self):
        return self.first_name
    
    @property
    def get_full_name(self): 
        return f"{self.first_name} {self.last_name}"
    
    def tokens (self):
        pass

class OneTimePassword(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)


    def __str__(self):
        return f"{self.user.first_name} - otp code"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.user.email