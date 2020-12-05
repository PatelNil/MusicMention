from django.shortcuts import render
from music.models import Album
from rest_framework.views import APIView
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework import  status
# Create your views here.

class index(APIView):
    def get(self,request):
        albums = Album.objects.all()
        serial = AlbumSerializer(albums,many=True)
        return Response(serial.data)
    def post(self,request):
        pass