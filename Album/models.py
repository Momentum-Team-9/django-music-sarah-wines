from django.db import models
from django.db.models.fields import DateTimeField
# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=255)
    album_photo = models.ImageField(upload_to='images', null=True, blank=True)
    created_at = DateTimeField(auto_now_add = True)
    release_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}, {self.artist}, {self.release_year}"
        
class Track(models.Model):
    title = models.CharField(max_length=250)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='track')

    def __str__(self):
        return f"{self.title}, {self.Album}"





