from django.contrib.auth.models import AbstractUser
# AbstractUser
from django.db import models
from django.shortcuts import render


class Shopper(AbstractUser):
    pass


class Profile(models.Model):
    username = models.OneToOneField(Shopper, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)

    # update_profile
    def update_profile(self):
        return render(self, 'accounts/update_profile.html')

    # delete_profile
    def delete_profile(self):
        return render(self, 'accounts/delete_profile.html')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


