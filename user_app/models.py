from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField(validators=[EmailValidator()])
    password = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    cnic = models.CharField(max_length=15, validators=[MinLengthValidator(13)], null=True, blank=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'custom_user'