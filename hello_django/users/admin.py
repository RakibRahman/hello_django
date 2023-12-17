from django.contrib import admin

# Register your models here.
from .models import User as UserTable

class UserAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email')
admin.site.register(UserTable,UserAdmin)