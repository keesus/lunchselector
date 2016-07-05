from django.contrib import admin
from lunchSelector.models import Menu,Order

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','menu_text','count','count_permanent']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['o_menu_text','date']




admin.site.register(Menu,MenuAdmin)
admin.site.register(Order,OrderAdmin)
# Register your models here.
