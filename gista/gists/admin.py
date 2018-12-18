from django.contrib import admin

from .models import Gist


@admin.register(Gist)
class GistAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'author',
        'body',
        'language',
    )
    list_filter = ('created', 'modified', 'author')