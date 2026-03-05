from .models import Singer , Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    # song_set = serializers.StringRelatedField(many=True,read_only=True)#names of songs
    # song_set = serializers.PrimaryKeyRelatedField(many=True,read_only=True)#ids of songs
    # song_set = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='songs-detail')#will create urls for songs
    # song_set = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='songs-detail')#will create urls for songs
    # song_set = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')#if duration instead of title then it will show duration of songs
    song_set = serializers.HyperlinkedIdentityField(view_name='songs-detail')#will create urls for songs






    class Meta:
        model = Singer
        fields = ['id','name','gender','song_set']