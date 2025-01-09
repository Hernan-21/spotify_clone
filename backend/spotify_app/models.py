from django.db import models # type: ignore

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
