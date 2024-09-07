from django.contrib import admin
from .models import *

# Register your models here.

class fooditemsAdmin(admin.ModelAdmin):
    list_display=['id','name','foodtype','price','desc','category','image']

admin.site.register(fooditems, fooditemsAdmin)