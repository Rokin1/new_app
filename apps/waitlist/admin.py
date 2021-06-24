from django.contrib import admin
from .models import WaitlistEntry

class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'updated_at')
    # list_filter = ('')
    search_fields = ('first_name','last_name')
    
    
    
admin.site.register(WaitlistEntry, WaitlistEntryAdmin)
