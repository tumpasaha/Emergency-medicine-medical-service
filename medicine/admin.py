from django.contrib import admin
from .models import *
# Register your models here.
class AddMedicine(admin.ModelAdmin):
    list_display = ('medicine_id','medicine_name','company_name','strength','pack_size','price_BDT','medicine_pic')

admin.site.register(Medicine,AddMedicine)

