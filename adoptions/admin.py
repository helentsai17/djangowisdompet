from django.contrib import admin

# Register your models here.
from .models import Pet

@admin.register(Pet) 
class PetAdmin(admin.ModelAdmin):
    #pass #for not override 
    list_display = ['name','species','breed','age', 'sex']