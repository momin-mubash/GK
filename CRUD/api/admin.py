from django.contrib import admin
from .models import Student

# Register your models here.
#This is a decorator.
@admin.register(Student)
#“Register the Student model with the admin site,
#and use the StudentAdmin class to control how it looks.”
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name' , 'roll' , 'city']