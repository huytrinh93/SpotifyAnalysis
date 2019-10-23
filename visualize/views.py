from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import sys
import spotipy
import spotipy.util as util
import json
import math
import matplotlib.pyplot as plt

def Convert_From_ms_To_minute(numb):
    # convert from ms to second
    numb = numb/1000
	
    #convert from second to minute
    minutes = math.floor(numb / 60)
    seconds = math.floor(numb % 60)
    return [minutes, seconds]
	
def Get_Exclude_and_Include_List(listA, listB):
	if(not(listA) or not(listB)):
		return [ ]
	#print(listA)
	#print(listB)
	exclude = [element for element in listA if element not in listB] + [element for element in listB if element not in listA]
	include = [element for element in listA if element in listB]
	return [exclude, include]

def Search_Item_on_Spotify(spotifyEngine, searchString):
	if(not(searchString)):
		return []
	
	results = spotifyEngine.search(searchString, limit=1)
	result = results['tracks']['items'][0]  # Find top result
	
	album_name = result['album']['name']  # Parse json dictionary
	artist = result['album']['artists'][0]['name']
	track_time = Convert_From_ms_To_minute(result['duration_ms'])
	track_name = result['name']
	popularity = result['popularity']
	#album_art = result['album']['images'][0]['url']	

	track_avail_market = result['available_markets']
	album_avail_market = result['album']['available_markets']
	
	item = {
		'albumName' : album_name,
		'artist' : artist,
		'trackName' : track_name,
		'trackTime' : track_time,
		'popularitie' : popularity,
		'trackMarket' : track_avail_market,
		'albumMarket' : album_avail_market,
	}
	return item

def index(request):	
	client_credentials_manager = util.oauth2.SpotifyClientCredentials('3dc7856c74e34c66bbcac293cfd18775', '51a6d9fede274298872af6c85313fa0b')

	spotifyEngine = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	compareResult = []
	result = Search_Item_on_Spotify(spotifyEngine,"Jay Z")
	compareResult.append(result)
	result = Search_Item_on_Spotify(spotifyEngine,"BTS")
	compareResult.append(result)	
	
	distinctLists = Get_Exclude_and_Include_List(compareResult[0]['trackMarket'], compareResult[1]['trackMarket'])
	labels = ['Not Popular in Region', 'Populate in Regions']
	colors = ['r', 'g']
	plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
	plt.show()

	context = {
		'compareResult' : compareResult,
		'distinctLists' : distinctLists,
	}
	return render(request,'app/index.html', context)