from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=30)
    contact = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.name}"


# Item in our store
class Item(models.Model):
    """model for item """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


class Store(models.Model):
    """model for store item"""
    date = models.DateTimeField(auto_now_add=True)
    item = models.ForiegnKey(Item)
    quantity = models.PositiveInterger()
    rate = models.PositiveInterger()

    def total(self):
        return self.quantity * self.rate
