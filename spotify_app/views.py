from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .spotify_client import get_spotify_client # type: ignore
from django.views.decorators.cache import cache_page # type: ignore

# Cachear la vista por 60 segundos para evitar demasiadas peticiones
@cache_page(60)
def index(request):
    try:
        spotify = get_spotify_client()
        
        # Hacer todas las peticiones en una sola función
        results = {
            'user': spotify.current_user(),
            'playlists': spotify.current_user_playlists(limit=10)['items'],  # Limitamos a 10 playlists
            'top_tracks': spotify.current_user_top_tracks(limit=5)['items'],  # Limitamos a 5 canciones
        }
        
        # Solo obtener current_playback si es necesario
        try:
            results['current_playback'] = spotify.current_playback()
        except:
            results['current_playback'] = None
            
        return render(request, 'spotify/index.html', results)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Cachear la vista de playlist por 60 segundos
@cache_page(60)
def playlist_detail(request, playlist_id):
    try:
        spotify = get_spotify_client()
        playlist = spotify.playlist(playlist_id)
        return render(request, 'spotify/playlist_detail.html', {
            'playlist': playlist
        })
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def now_playing(request):
    spotify = get_spotify_client()
    # Obtener la canción actual
    current = spotify.current_playback()
    
    return render(request, 'spotify/now_playing.html', {
        'track': current
    })

def callback(request):
    return redirect('index')
