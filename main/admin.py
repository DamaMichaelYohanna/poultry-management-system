from django.contrib import admin

from .models import Item, Store, Farm, Order, Invoice, InvoiceProduct, GProduct, GProductCategory

admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Farm)
admin.site.register(Order)
admin.site.register(Invoice)
admin.site.register(InvoiceProduct)
admin.site.register(GProduct)
admin.site.register(GProductCategory)