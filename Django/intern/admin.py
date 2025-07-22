from django.contrib import admin
from . models import intern
# Register your models here.

@admin.register(intern)
class InternAdmin(admin.ModelAdmin):
    list_display=['id','firstname','lastname','email','phone','location','college','job','myfile']