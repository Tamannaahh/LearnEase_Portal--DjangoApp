from django.contrib import admin
from . models import * 

# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)


# Schedule Admin Configuration
from django.utils.html import format_html
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'day', 'time', 'created_at', 'updated_at', 'day_colored')

    def day_colored(self, obj):
        colors = {
            'Sunday': 'red',
            'Monday': 'blue',
            'Tuesday': 'green',
            'Wednesday': 'orange',
            'Thursday': 'purple',
            'Friday': 'cyan',
            'Saturday': 'yellow',
        }
        return format_html(
            '<span style="color: {};">{}</span>',
            colors.get(obj.day, 'black'),  # Default to black if day not found
            obj.day
        )
    day_colored.short_description = 'Day'

