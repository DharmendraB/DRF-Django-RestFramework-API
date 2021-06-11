from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll','city']
    search_fields = ['name','city']
    list_filter = ["city"] 
