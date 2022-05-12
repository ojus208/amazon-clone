from django.contrib import admin
from .models import Offer, Products, Deals, Address, Auth_user, Orders, Cart, Trending

# Register your models here.

admin.site.register(Offer)
admin.site.register(Products)
admin.site.register(Deals)
admin.site.register(Address)
admin.site.register(Auth_user)
admin.site.register(Orders)
admin.site.register(Trending)
admin.site.register(Cart)