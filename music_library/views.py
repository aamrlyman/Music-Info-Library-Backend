from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import music_library 
from .models import Music_Library
from music_library import serializers
from .serializers import Music_LibrarySerializer


# Create your views here.
@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        music_library = Music_Library.objects.all()
        serializer = Music_LibrarySerializer(music_library, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = Music_LibrarySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def song_detail(request, pk):
    song = get_object_or_404(Music_Library, pk=pk)
    if request.method == 'GET':
        serializer = Music_LibrarySerializer(song);
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = Music_LibrarySerializer(song, data=request.data);
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
             song.delete()
             return Response(status = status.HTTP_204_NO_CONTENT)

# @api_view(["PUT"])
# def like_song(request, pk):
#     song = get_object_or_404(Music_Library, pk=pk)
#     if request.method == "PUT":
#         song.likes += 1
#         serializer = Music_LibrarySerializer(song, data=request.data);
#         serializer.is_valid(raise_exception=True)
#         serializer.save(update_fields=["likes"])
#         return Response(serializer.data)

@api_view(["PUT"])
def like_song(request, pk):
    song = Music_Library.objects.filter(pk=pk).update(likes= 1)
    request = song
    return Response(request)

    #     if request.method == "PUT":
#         song.likes += 1
#         serializer = Music_LibrarySerializer(song, data=request.data);
#         serializer.is_valid(raise_exception=True)
#         serializer.save(update_fields=["likes"])
#         return Response(serializer.data)
   
