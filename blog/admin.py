from django.contrib import admin
from blog.models import Menu, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)