from django.contrib import admin
from .models import ItemType, PantryItem

# Models
admin.site.register(ItemType)
admin.site.register(PantryItem)