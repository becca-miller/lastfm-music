""" 
Create a list of tracks that have been listened to on loop, ordered by date,
using last.fm listening history

"""
import pandas as pd
import os

#Set directory and file name here
path = 'YOUR_FILE_PATH'
#You can use my listening history, stored here, or generate your own using lastfm_data
file_name = 'data/listening_history.csv'
os.chdir(path) 

#Read in file containing listening history
history = pd.read_csv(path+file_name, encoding='utf-8')

#Generate a list of all songs with >=cutoff subsequent plays
def looped_tracks(hist,cutoff,repeats=1, chrono=0):
    """Returns a dataframe containing tracks that have were listened to on repeat,
    including title, artist, album, date, and number of consecutive plays, in
    chronological or reverse chronological order.

    Keyword arguments:
    hist -- dataframe containing listening history
    cutoff -- the minimum number of consecutive plays to be included
    repeats -- whether repeats are allowed. If allowed (1), tracks can be included
               in the dataframe at multiple points. If not (0), only the earliest 
               instance will be included (default 1)
    chrono -- Chronological order (1) or reverse chronological order (default 0)

    """
    
    count = 0
    prev = []

    #Add play counts for consecutive tracks in listening history
    for i in hist.index:
        if prev==[hist.at[i,'track'], hist.at[i,'artist']]:
            count = count+1
        else:
            prev = [hist.at[i,'track'], hist.at[i,'artist']]
            count=1
        hist.at[i,'count'] = count
    
    #Filter to only tracks with >=cutoff plays
    looped = [hist.loc[i] for i in hist.index if hist.at[i,'count']>=cutoff]

    #Sort chronologically, so for repeats, earlier songs are added first
    looped = looped[::-1]    

    result = [] 
    tracks = [] 
    prev = []
    
    #Add final song selections to the results list
    for i in range(0,len(looped)):
        track = [looped[i].track,looped[i].artist] #current track
        #Repeats not allowed: only add songs if they're not yet in list
        if repeats==0 and track not in tracks: 
            tracks.append(track)
            result.append(looped[i])
        #Repeats allowed: add if song is not the same as preceding in list
        elif repeats==1 and track!=prev:
            prev = track
            result.append(looped[i])

    #Reorder to newest first
    if chrono==0:
        result = result[::-1]

    #Convert to dataframe and clean
    result = pd.DataFrame(result)
    result = result[['track','artist','album','date','count']]  
        
    return result


#Get list of songs with at least 5 consecutive plays, allowing for repeats
looped_rep = looped_tracks(history,cutoff=5,repeats=1,chrono=0)
looped_rep = pd.DataFrame(looped_rep)
looped_rep.to_csv('data/looped_rep.csv',index=None,encoding='utf-8')

#Similar call, this time disallowing repeats
looped_norep = looped_tracks(history,cutoff=5,repeats=0,chrono=0)
looped_norep = pd.DataFrame(looped_norep)
looped_norep.to_csv('data/looped_norep.csv',index=None,encoding='utf-8')