import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'eamonwong'

token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

# Create the playlist
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)

user_input = input("Enter the songs: ")
list_of_songs = []

while user_input != 'quit':
    result = spotifyObject.search(q=user_input)
    # print(json.dumps(result,sort_keys=4,indent=4)
    list_of_songs.append(result['track']['items'][0]['uri'])
    user_input = input("'Enter the song: ")

# Find new playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

# Add songs
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)
