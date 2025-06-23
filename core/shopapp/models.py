from django.db import models

from loginapp.models import Address, User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=True)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False, blank=False)


class Shop(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=True)
    logo_url = models.CharField(max_length=300, null=True, blank=True)
    shop_type = models.ForeignKey('CShop', on_delete=models.CASCADE, null=False, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

class CShop(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=True)
    
class Transaction(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    buyer_iduser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer', null=False, blank=False)
    seller_iduser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller', null=False, blank=False)
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE, null=False, blank=False)
    status = models.ForeignKey('CTransactionStatus', on_delete=models.CASCADE, null=False, blank=False)
    payment_method = models.ForeignKey('CPaymentMethod', on_delete=models.CASCADE, null=False, blank=False)

class CTransactionStatus(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=True)

class CPaymentMethod(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=True)

class Review(models.Model):
    rating = models.IntegerField(null=False, blank=False)
    comment = models.CharField(max_length=200, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)