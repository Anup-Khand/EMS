from django.contrib import admin
from .models import subject
# Register your models here.
@admin.register(subject)
class subjectAdmin(admin.ModelAdmin):
    list_display = ['subid', 'name']