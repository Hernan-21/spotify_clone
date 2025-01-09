from django.contrib import admin # type: ignore
from .models import Playlist

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'spotify_id', 'created_at')
    search_fields = ('name', 'spotify_id')
