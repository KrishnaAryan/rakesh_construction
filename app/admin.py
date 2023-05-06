from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'address', 'service', 'date_requested')
    search_fields = ('name', 'phone_number', 'email', 'address', 'service')
    
admin.site.register(Customer, CustomerAdmin)


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage

@admin.register(LatestProject)
class LatestProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ['project_name', 'location', 'project_start_date', 'project_end_date']
