from django.contrib import admin
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer_name', 'date')
    list_filter = ('title', 'lecturer_name')
    search_fields = ('name',)
    
    
    
admin.site.register(Lecture, LectureAdmin, )
        
        
        