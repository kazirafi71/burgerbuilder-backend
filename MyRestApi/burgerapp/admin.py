from django.contrib import admin
from .models import UserProfile, Order, Ingredient, CustomerDetails

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(CustomerDetails)
