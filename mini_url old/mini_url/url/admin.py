from django.contrib import admin

from .models import MiniURL


class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'code', 'date', 'pseudo', 'nb_acces')
    list_filter = ('url',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_field = ('url',)


admin.site.register(MiniURL, MiniURLAdmin)
