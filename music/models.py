from django.db import models
from django.urls import reverse
from django.shortcuts import  redirect

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=20)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('music:details',kwargs={'pk':self.pk})
    def __str__(self):
        return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)#if we delete album then songs will also will be deleted.
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_fav = models.BooleanField(default=False)
    def __str__(self):
        return self.song_title
    def get_absolute_url(self):
        return reverse('music:details',kwargs={'pk':self.album.id})
