from django.contrib import admin

from .models import Item, Store, Farm, Product, Category, Order, Invoice, InvoiceProduct

admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Farm)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Invoice)
admin.site.register(InvoiceProduct)