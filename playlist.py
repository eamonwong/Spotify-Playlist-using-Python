import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'eamonwong'

# Obtain the authentication token for the authenticated user
token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

# Get information about the authenticated user
user_info = spotifyObject.current_user()
authenticated_username = user_info['id']

# Create the playlist for the authenticated user
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(user=authenticated_username, name=playlist_name, public=True, description=playlist_description)

user_input = input("Enter the songs: ")
list_of_songs = []

while user_input.lower() != 'quit':
    result = spotifyObject.search(q=user_input)
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input("Enter the song: ")export SPOTIPY_REDIRECT_UR

# Find the newly created playlist for the authenticated user
pre_playlists = spotifyObject.current_user_playlists()
playlist = pre_playlists['items'][0]['id']

# Add songs to the authenticated user's playlist
spotifyObject.playlist_add_items(playlist_id=playlist, items=list_of_songs)

# Have to export these in terminal for project to work
# export SPOTIPY_CLIENT_ID
# export SPOTIPY_CLIENT_SECRET
# export SPOTIPY_REDIRECT_URI
