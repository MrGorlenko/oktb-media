from django.contrib import admin
from .models import Theme, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'theme', 'is_active', 'hot',)
    list_display_links = ('date',)
    list_editable = ('title', 'is_active',)


admin.site.register(Theme)
admin.site.register(Article, ArticleAdmin)
