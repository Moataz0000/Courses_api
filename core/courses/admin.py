from django.contrib import admin
from .models import Subject, Course, Module




@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}    
    
    
class ModuleInline(admin.StackedInline):
    model = Module    
    
    

@admin.register(Course)    
class Course(admin.ModelAdmin):    
    list_display = ['title', 'subject', 'created', 'status']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    inlines = [ModuleInline]
    readonly_fields = ['slug']

    
    
admin.site.register(Module)    