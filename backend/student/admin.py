from django.contrib import admin
from .models import Students
# Register your models here.
@admin.register(Students)
class studentAdmin(admin.ModelAdmin):
    list_display = ['stuid', 'name', 'email', 'password', 'phone', 'address', 'gender', 'profile_pic']