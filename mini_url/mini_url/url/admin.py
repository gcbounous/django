from django.contrib import admin

from .models import MiniURL


class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('url_longue', 'code')
    list_filter = ('url_longue',)
    date_hierarchy = 'date_creation'
    ordering = ('date_creation',)
    search_field = ('url_longue',)


admin.site.register(MiniURL, MiniURLAdmin)
