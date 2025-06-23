from django.db import models

from loginapp.models import User
from shopapp.models import Item, Transaction

# Create your models here.
class DeliveryMethod(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=False, blank=False)

class CDeliveryMethod(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)