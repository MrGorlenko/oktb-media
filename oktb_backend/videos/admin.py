from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'about', 'video',)
    list_display_links = ('title',)
    list_editable = ('about',)
    search_fields = ('title', 'about',)
    list_filter = ('title', 'date')


admin.site.register(Video, VideoAdmin)
