from django.contrib import admin
from django.contrib.auth.models import User

from apps.models import Course, Category, Cars, Cart, Transaction
from django.contrib import admin

# Register your models here.
admin.site.site_header = "Izzat Admin"
admin.site.site_title = "Izzat Admin Portal"
admin.site.index_title = "Welcome to Izzat Researcher Portal"

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display =  "photo", "product", "Qty", "price", "total"

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display =  "id", "date", "name", "amount", "status"

