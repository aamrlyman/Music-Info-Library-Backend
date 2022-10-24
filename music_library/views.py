from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import music_library 
from .models import Song
from music_library import serializers
from .serializers import SongSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        music_library = Song.objects.all()
        serializer = SongSerializer(music_library, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = SongSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(song);
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SongSerializer(song, data=request.data);
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
             song.delete()
             return Response(status = status.HTTP_204_NO_CONTENT)

# @api_view(["PUT"])
# def like_song(request, pk):
#     song = get_object_or_404(Song, pk=pk)
#     if request.method == "PUT":
#         song.likes += 1
#         serializer = SongSerializer(song, data=request.data);
#         serializer.is_valid(raise_exception=True)
#         serializer.save(update_fields=["likes"])
#         return Response(serializer.data)

# # @api_view(["PUT"])
# # def like_song(request, pk):
# #     song = Song.objects.get(id=pk)
# #     song.update(likes = song.likes + 1)
# #     request = song
#     return Response(request)

    #     if request.method == "PUT":
#         song.likes += 1
#         serializer = SongSerializer(song, data=request.data);
#         serializer.is_valid(raise_exception=True)
#         serializer.save(update_fields=["likes"])
#         return Response(serializer.data)
   
