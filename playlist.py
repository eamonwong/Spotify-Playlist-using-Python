import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = #client_id
client_secret = #client_secret
redirect_uri = #redirect_uri
scope = 'playlist-modify-public user-library-read'  # Modified to combine playlist modification and user library read scopes

# Authenticate with Spotify
token = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
)
spotifyObject = spotipy.Spotify(auth_manager=token)

# Get information about the authenticated user
user_info = spotifyObject.current_user()
authenticated_username = user_info['id']

# Create the playlist for the authenticated user
playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

playlist = spotifyObject.user_playlist_create(user=authenticated_username, name=playlist_name, public=True,
                                              description=playlist_description)
playlist_id = playlist['id']

# Add songs to the playlist
list_of_songs = []
user_input = input("Enter a song name (or 'quit' to finish): ")

while user_input.lower() != 'quit':
    result = spotifyObject.search(q=user_input, type='track', limit=15)
    tracks = result['tracks']['items']

    if tracks:
        for i, track in enumerate(tracks):
            print(f"{i + 1}. {track['name']} by {track['artists'][0]['name']}")

        # Allow the user to type "n/a" if the song is not in the list
        selection = input("Enter the number of the correct song (or 'n/a' if the song is not listed): ")

        if selection.lower() == 'n/a':
            print("Skipping this song.")
        else:
            try:
                selection = int(selection) - 1
                if 0 <= selection < len(tracks):
                    list_of_songs.append(tracks[selection]['uri'])
                else:
                    print("Invalid selection. Skipping this song.")
            except ValueError:
                print("Invalid input. Skipping this song.")
    else:
        print("No results found.")

    user_input = input("Enter another song name (or 'quit' to finish): ")

# Add the selected songs to the playlist
if list_of_songs:
    spotifyObject.playlist_add_items(playlist_id=playlist_id, items=list_of_songs)
    print(f"Added {len(list_of_songs)} songs to the playlist '{playlist_name}'.")
else:
    print("No songs were added to the playlist.")
