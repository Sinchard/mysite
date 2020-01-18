from django.contrib import admin
from .models import Fiction, Chapter, Content

class FictionAdmin(admin.ModelAdmin):
    list_display = ('fiction_id', 'url', 'name', 'updated')
    list_filter = ('updated',)
    search_fields = ('fiction_id', 'name')
    date_hierarchy = 'updated'
    ordering = ['fiction_id']
admin.site.register(Fiction, FictionAdmin)

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('fiction_id', 'chapter_id','url', 'name', 'updated')
    list_filter = ('fiction_id','updated')
    search_fields = ('fiction_id', 'chapter_id','name')
    date_hierarchy = 'updated'
    ordering = ['fiction_id', 'chapter_id',]
admin.site.register(Chapter,ChapterAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('fiction_id', 'chapter_id','content', 'updated')
    list_filter = ('fiction_id','updated')
    search_fields = ('fiction_id', 'chapter_id','content')
    date_hierarchy = 'updated'
    ordering = ['fiction_id', 'chapter_id',]
admin.site.register(Content,ContentAdmin)