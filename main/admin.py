from django.contrib import admin

from .models import Item, Store, Farm

admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Farm)