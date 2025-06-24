from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, null=False, blank=False)
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    picture_url = models.CharField(max_length=300, null=True, blank=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, default=1)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True, blank=True)

class Role(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.BigIntegerField(null=False, blank=False)
    ext_number = models.IntegerField(null=False, blank=False)
    int_number = models.IntegerField(null=False, blank=False)
    country = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)