from django.contrib import admin
from .models import Allergens,Categories,MenuItem
# Register your models here.




admin.site.register(Categories)
admin.site.register(Allergens)
admin.site.register(MenuItem)