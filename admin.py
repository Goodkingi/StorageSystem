from django.contrib import admin
from django.db import models
from .models import Product, Store, Department, Staff


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter = ("name", "brand", "details", "serial", "quantity","categorie","condition","status")
    list_display = ("name", "brand", "details", "serial", "quantity","categorie","condition","status")


admin.site.register(Product, ProductAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_filter = ("store_name", "store_address")
    list_display = ("store_name", "store_address")


admin.site.register(Store, StoreAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_filter = ("department_name", "department_address")
    list_display = ("department_name", "department_address")


admin.site.register(Department, DepartmentAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ("staff_first_name", "staff_last_name", "username")
    list_filter = ("staff_first_name", "staff_last_name")


admin.site.register(Staff, StaffAdmin)

# class InventoryAdmin(admin.ModelAdmin):
#     list_display = ("category","name","barcode","serial_number","quantity","date" ,"brand",
#                     "details" ,"condition","status", "image","files","department", "address","staff",)
#     list_filter = ("category","name","brand","department","condition","status","address","staff",)

# class CategorieAdmin(admin.ModelAdmin):
#     list_display =("category",)
#     list_filter = ("category",)

# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ("type","item","quantity","date","user")
#     list_filter = ("type","item","quantity","date",)

# class OrderAdmin(admin.ModelAdmin):
#     list_display =("staffname","item","quantity","address","date",)
#     list_filter = ("item","quantity","address","date",)

# class UploadAdmin(admin.ModelAdmin):
#     list_display = ("user_image",)
#     list_filter = ( "user_image",)
# admin.site.register(Store,StoreAdmin)
# admin.site.register(Staff,StaffAdmin)
# admin.site.register(Department,DepartmentAdmin)
# admin.site.register(Categorie,CategorieAdmin)
# admin.site.register(Inventory,InventoryAdmin)
# admin.site.register(Transaction,TransactionAdmin)
# admin.site.register(Order,OrderAdmin)
# admin.site.register(upload,UploadAdmin)
# # admin.site.register(Comments)
# # admin.site.register(QuestionAnswer)
# # admin.site.register(Notes)
# # admin.site.register(Author)
# # admin.site.register(Groups)
# # admin.site.register(Semester)


# ###example from chat GPT
# from django.contrib import admin
# from .models import Item, Transaction, User

# admin.site.register(Item)
# admin.site.register(Transaction)
# admin.site.register(User)
