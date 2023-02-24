from django.contrib import admin
from apis.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = [f.name for f in User._meta.get_fields()]
    search_fields = ['name', 'email']
    list_filter = ['created_at', 'updated_at', 'gender']
    list_per_page = 20
    
admin.site.register(User, UserAdmin)
admin.site.register(Address)
