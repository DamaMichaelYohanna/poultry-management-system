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

    def __str__(self):
        return f'{self.name}'


class Store(models.Model):
    """model for store item"""
    date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.item.name}'

    def total(self):
        return self.quantity * self.rate


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    """model for product to have been added to cart"""
    product = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now=True)


class InvoiceProduct(models.Model):
    """models for product that are sold out"""
    name = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField(default=0)
    ref = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def total():
        return quantity * price


class Invoice(models.Model):
    """model for the various invoices"""
    ref = models.PositiveIntegerField()
    customer = models.CharField(max_length=20)
    contact = models.CharField(max_length=12)
    payment = models.CharField(max_length=10, default='cash')
    goods = models.ManyToManyField(InvoiceProduct)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ref)
