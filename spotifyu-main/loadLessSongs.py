""" 
artist_id varchar(22) NOT NULL, join based off of artist_id with artist --> group by artist_id --> count songs by each artist and display artist name with total songs contributed
album_id varchar(22) NOT NULL, join based off of album_id with album --> group by album_id --> filter only albums in 2019 and display album name and sort by date released 
"""

''' We are making song table to have attributes song_id, song_name, release_year, artist_id, and album_id'''

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

file1 = open('lessSongsList.txt', 'r')
Lines = file1.readlines()

for i in range(1, len(Lines)):
    song_id1 = Lines[i].strip()
    output = 'spotify:track:{}'.format(song_id1)

    track = sp.track(output)

    song_name = track['name'] # change to where songs is 
    release_date = track['album']['release_date']
    
    #added new attributes
    album_id = track['album']['id']
    
    artistList = track['artists']
    arrId = []
    # the artistName array and Artist ID array
    for i in artistList:
        arrId.append(i['id'])


    for i in range(len(artistList)):
        add_song_artists = ("INSERT IGNORE INTO SongsArtists "
                    "(song_id, song_name, release_date, artist_id, album_id) "
                    "VALUES (%(data_song_id)s, %(data_song_name)s, %(data_release_date)s, %(data_artist_id)s, %(data_album_id)s)")

        data_song_artists = {
            'data_song_id': song_id1,
            'data_song_name': song_name,
            'data_release_date': release_date,
            'data_artist_id': arrId[i],
            'data_album_id': album_id
        }
        # Insert new employee
        cursor.execute(add_song_artists, data_song_artists)

        # Make sure data is committed to the database
        cnx.commit()

file1.close()

cursor.close()
cnx.close()

