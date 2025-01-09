from django.http import JsonResponse # type: ignore
from django.views.decorators.cache import cache_page # type: ignore
from .spotify_client import get_spotify_client
import logging

logger = logging.getLogger(__name__)

@cache_page(60)
def index(request):
    try:
        spotify = get_spotify_client()
        logger.info("Obteniendo datos de Spotify...")
        
        data = {
            'user': spotify.current_user(),
            'playlists': spotify.current_user_playlists()['items'],
            'top_tracks': spotify.current_user_top_tracks(limit=10)['items'],
            'new_releases': spotify.new_releases(limit=20)['albums']['items'],
            'categories': spotify.categories()['categories']['items']
        }
        
        logger.info("Datos obtenidos exitosamente")
        return JsonResponse(data)
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=400)

@cache_page(60)
def playlist_detail(request, playlist_id):
    try:
        spotify = get_spotify_client()
        playlist = spotify.playlist(playlist_id)
        return JsonResponse(playlist, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def callback(request):
    return JsonResponse({'status': 'success'})

@cache_page(60)
def search(request):
    query = request.GET.get('q', '')
    try:
        spotify = get_spotify_client()
        results = spotify.search(
            q=query,
            type='track,artist,album,playlist',
            limit=20
        )
        return JsonResponse(results)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
