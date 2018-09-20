""" Download data from last.fm account """

import requests
import pandas as pd

#Set this to your save path
path = 'YOUR_FILE_PATH'
file_name = 'data/listening_history.csv'

#Replace with your key and history
key = 'YOUR_API_KEY'
username = 'YOUR_USERNAME'


def get_history(username, key,limit=200,page=1):
    """Returns Last.Fm listening history

    Keyword arguments:
    username -- last.fm username
    key -- last.fm API key
    limit -- the number of tracks to request at once (default 200)
    page -- the page to start request (default 1)

    """
    url = 'https://ws.audioscrobbler.com/2.0/?method=user.get{}&user={}&api_key={}&limit={}&page={}&format=json'
    method = 'recenttracks'
    request_url = url.format(method, username, key, limit, page)
    responses = []
    track_names = []
    track_mbids = []
    artist_names = []
    artist_mbids = []
    album_names = []
    album_mbids = []
    timestamps = []
    
    #get the total number of pages
    request_url = url.format(method, username, key, limit,page)
    response = requests.get(request_url).json()
    pages = int(response[method]['@attr']['totalPages'])
    
    for page in range(1,pages+1):
        print('Appending page '+str(page)+' of '+ str(pages))
        request_url = url.format(method, username, key, limit, page)
        responses.append(requests.get(request_url))
    
    # parse the fields out of each scrobble in each page (aka response) of scrobbles
    for response in responses:
        tracks = response.json()
        for track in tracks[method]['track']:
            if 'date' in track.keys(): #ie tracking is complete
                track_names.append(track['name'])
                track_mbids.append(track['mbid'])
                artist_names.append(track['artist']['#text'])
                artist_mbids.append(track['artist']['mbid'])
                album_names.append(track['album']['#text'])
                album_mbids.append(track['album']['mbid'])
                timestamps.append(track['date']['uts'])
    
    # create and populate a dataframe to contain the data
    history = pd.DataFrame()
    history['track'] = track_names
    history['mbid'] = track_mbids
    history['artist'] = artist_names
    history['artist_mbids'] = artist_mbids
    history['album'] = album_names
    history['album_mbids'] = album_mbids
    history['timestamp'] = timestamps
    history['datetime'] = pd.to_datetime(history['timestamp'].astype(int), unit='s')
    history['date']=history['datetime'].dt.date
    
    return history

#Function calls to get listening history and save to computer
history = get_history(username=username,key=key)
history.to_csv(path+file_name, index=None, encoding='utf-8')