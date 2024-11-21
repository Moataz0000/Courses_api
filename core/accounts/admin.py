from django.contrib import admin
from .models import InstructorProfile




@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    pass