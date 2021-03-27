import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from datetime import date, datetime, timedelta
import mysql.connector

auth_manager = SpotifyClientCredentials('f3dc4f3802254be091c8d8576961bc9d', 'b51d135ad7104add8f71933197e9cc14')
sp = spotipy.Spotify(auth_manager=auth_manager)

cnx = mysql.connector.connect(user='root', password='1234',
                              host='104.197.65.16',
                              database='main')
cursor = cnx.cursor()

file1 = open('songs.txt', 'r')
Lines = file1.readlines()

for i in range(1, len(Lines)):
    song_id1 = Lines[i].strip()
    output = 'spotify:track:{}'.format(song_id1)

    track = sp.track(output)

    song_name = track['name'] # change to where songs is 
    release_datee = track['album']['release_date']

    add_song = ("INSERT IGNORE INTO Songs "
                "(song_id, name, release_date) "
                "VALUES (%(song_id)s, %(name)s, %(release_date)s)")

    data_song = {
        'song_id': song_id1,
        'name': song_name,
        'release_date': release_datee
    }
    # Insert new employee
    cursor.execute(add_song, data_song)

    # Make sure data is committed to the database
    cnx.commit()

file1.close()

cursor.close()
cnx.close()
