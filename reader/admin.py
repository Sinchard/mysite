from django.contrib import admin
from .models import Fiction, Chapter, Content

class FictionAdmin(admin.ModelAdmin):
    list_display = ('fiction_id', 'url', 'name', 'updated')
    list_filter = ('updated',)
    search_fields = ('fiction_id', 'name')
    date_hierarchy = 'updated'
    ordering = ['fiction_id']
admin.site.register(Fiction, FictionAdmin)

admin.site.register(Chapter)
admin.site.register(Content)