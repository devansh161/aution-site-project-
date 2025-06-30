from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified', 'created_at')  # Customize fields shown in the admin list view

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Contact)

admin.site.register(Product)

admin.site.register(Bid)
