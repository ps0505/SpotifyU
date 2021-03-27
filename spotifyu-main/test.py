import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date, datetime, timedelta

auth_manager = SpotifyClientCredentials('f3dc4f3802254be091c8d8576961bc9d', 'b51d135ad7104add8f71933197e9cc14')
sp = spotipy.Spotify(auth_manager=auth_manager)
output = 'spotify:track:{}'.format('31AOj9sFz2gM0O3hMARRBx')
track = sp.track('034DO7YYTxeywhjWeetfu7')
print(track['name'])