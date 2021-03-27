import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date, datetime, timedelta
import mysql.connector
import io

auth_manager = SpotifyClientCredentials('f3dc4f3802254be091c8d8576961bc9d', 'b51d135ad7104add8f71933197e9cc14')
sp = spotipy.Spotify(auth_manager=auth_manager)

cnx = mysql.connector.connect(user='root', password='1234',
                              host='104.197.65.16',
                              database='main')
cursor = cnx.cursor()

file1 = open('newSongList.txt', 'r')
Lines = file1.readlines()
#file2 = io.open('output.json', 'w', encoding="utf-8")


for i in range(1, len(Lines)):
    track_id = Lines[i].strip()
    output = 'spotify:track:{}'.format(track_id)

    track = sp.track(output)

    artistList = track['artists']

    #print(len(track['artists']))  #this outputs 3
    arrArtist = []
    arrId = []
    # the artistName array and Artist ID array
    for i in artistList:
        arrArtist.append(i['name'])
        arrId.append(i['id'])

    #print(arrArtist)
    #print(arrId)
    
    #testing purposes output.json has the output for this stuff
    #for item in arrArtist:
    #    file2.write("%s, " % item)
    #file2.write('\n')
    #for item in arrId:
    #    file2.write("%s, " % item)
    #file2.write('\n')
    #file2.write('\n')

    for i in range(len(artistList)):
        add_artist = ("INSERT IGNORE INTO Artists "
                    "(artist_id, artist_name) "
                    "VALUES (%(data_artist_id)s, %(data_artist_name)s)")

        data_artist = {
            'data_artist_id': arrId[i],
            'data_artist_name': arrArtist[i]
        }
        # Insert new employee
        cursor.execute(add_artist, data_artist)

        # Make sure data is committed to the database
        cnx.commit()

file1.close()
# file2.close()

cursor.close()
cnx.close()
