from django.contrib import admin
from .models import Leader, LeaderCategory


class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'link', 'audience', 'job', 'mail', 'top')
    list_display_links = ('name',)
    list_editable = ('audience', 'job', 'mail',)
    search_fields = ('name', 'job', 'top', 'category__title',)
    list_filter = ('category', 'job', 'top')


admin.site.register(Leader, LeaderAdmin)
admin.site.register(LeaderCategory)
