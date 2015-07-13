from django.contrib import admin
from article.models import Article, Tag
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'date_time')
    search_fields = ('title',  'content')
    list_filter = ('date_time',)
    raw_id_fields = ('tag',)
    date_hierarchy = 'date_time'


admin.site.register(Article, MarkdownModelAdmin)
admin.site.register(Tag)
