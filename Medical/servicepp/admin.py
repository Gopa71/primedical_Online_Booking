from django.contrib import admin
from .models import  Service,Product,Home
# Register your models here.

admin.site.register(Home)

class ServiceAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}


admin.site.register(Service,ServiceAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','desc','slug','photo','available']
    list_editable=['available']
    list_per_page=20
    prepopulated_fields={'slug':('name',)}

admin.site.register(Product,ProductAdmin)


