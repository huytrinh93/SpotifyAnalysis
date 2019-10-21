from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import sys
import spotipy
import spotipy.util as util

def index(request):
	#token = util.oauth2.SpotifyClientCredentials(client_id='3dc7856c74e34c66bbcac293cfd18775', client_secret='51a6d9fede274298872af6c85313fa0b')

	#cache_token = token.get_access_token()
	#spotify = spotipy.Spotify(cache_token)

	#results1 = spotify.user_playlist_tracks(USER, PLAY_LIST, limit=100, offset=0)
	
	client_credentials_manager = util.oauth2.SpotifyClientCredentials('3dc7856c74e34c66bbcac293cfd18775', '51a6d9fede274298872af6c85313fa0b')

	spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	results = spotify.search("Boys", limit=1)

	results = results['tracks']['items'][0]  # Find top result
	album = results['album']['name']  # Parse json dictionary
	artist = results['album']['artists'][0]['name']
	artists = results['album']['artists']
	song_title = results['name']
	album_art = results['album']['images'][0]['url']

	context = {'artists': artist}
	return render(request,'app/index.html', context)