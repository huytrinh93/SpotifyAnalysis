from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import sys
import spotipy
import spotipy.util as util
import json

def index(request):	
	client_credentials_manager = util.oauth2.SpotifyClientCredentials('3dc7856c74e34c66bbcac293cfd18775', '51a6d9fede274298872af6c85313fa0b')

	spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	results = spotify.search("Boys", limit=1)

	result0 = results['tracks']['items'][0]  # Find top result
	
	album = result0['album']['name']  # Parse json dictionary
	artist = result0['album']['artists'][0]['name']
	artists = result0['album']['artists']
	song_title = result0['name']
	album_art = result0['album']['images'][0]['url']
	
	pretty_data = json.dumps(results['tracks']['items'], sort_keys=True, indent=4)

	context = {
		'results' : pretty_data,
		'artists': artist,
		'albums' : album,
	}
	return render(request,'app/index.html', context)