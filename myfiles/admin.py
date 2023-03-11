from django.contrib import admin

from myfiles.models import *
# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Type, AdminType)

class AdminMax(admin.ModelAdmin):
    list_display = ['id','nomi','narxi','tur','rasmi','text']
admin.site.register(Maxsulot,AdminMax)


class AdminMenu(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Menu, AdminMenu)


class AdminUser(admin.ModelAdmin):
    list_display = ['id','ism','fam','username','tg_id','text']
admin.site.register(Azolar, AdminUser)
