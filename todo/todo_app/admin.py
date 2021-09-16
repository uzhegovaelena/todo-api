from django.contrib import admin
from .models import Task


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit', 'title', 'description', 'date', 'done')
    list_filter = ('done', 'unit')
    list_display_links = ('id', 'title')
    list_editable = ('done',)
    search_fields = ('id', 'title', 'description')


admin.site.register(Task, TodoAdmin)
