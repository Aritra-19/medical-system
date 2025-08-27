from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100, blank=True)
    last_name=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to='user_picture', default='default.jpg')
    date_of_birth=models.DateField(blank=True, null=True)
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    verified=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def clean(self):
        if not self.first_name or not self.last_name or not self.date_of_birth or not self.phone_number:
            raise ValidationError("All fields must be filled before saving the profile.")

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)