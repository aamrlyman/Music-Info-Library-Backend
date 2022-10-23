from rest_framework import serializers
from .models import Music_Library

class Music_LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_Library
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre', 'likes']
        depth = 1

    super_type_id = serializers.IntegerField(write_only = True)