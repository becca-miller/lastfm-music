# Exploring your Last.fm listening history

Last.fm is a website that that tracks your music listening history. In this repo, I'm creating tools to explore your listening history. All data files generated from these scripts, using my account, are included in the [data folder](https://github.com/becca-miller/lastfm-music/tree/master/data).

## [consecutive_plays.py](https://github.com/becca-miller/lastfm-music/blob/master/consecutive_plays.py)

I have a habit of listening to the tracks I love on loop. I try to keep track of these particular songs with a playlist, according to when I listened to them, but unsurprisingly, it's a hard thing to manually track. This script is intended to automate this process. 

The script takes your last.fm listening history and generates a list of songs you've listened to on loop, including the number of consecutive plays and the date listened. The results are returned in reverse chronological order by default, but can also be ordered chronologically. You can decide whether you want to include only the first time a track is listened to on loop, or if you want to allow for repeated listens. Allowing for repeats can let you see the ebb and flow of your interest in a song (and I for one am in the habit of going back to the same song), while only allowing the first instance makes it easier to identify when you first grew to love a song. You can also specify the number of loops required for a song to be included in the output.

You can run this file using [listening_history.csv](https://github.com/becca-miller/lastfm-music/blob/master/data/listening_history.csv) or by generating your own history file using [last_fm_data.py](https://github.com/becca-miller/lastfm-music/blob/master/lastfm_data.py). 

My output, using a cutoff of 5 loops, is stored with repeats in [looped_rep.csv](https://github.com/becca-miller/lastfm-music/blob/master/data/looped_rep.csv) and without repeats in [looped_norep.csv](https://github.com/becca-miller/lastfm-music/blob/master/data/looped_norep.csv). To give you a taste, here is the head of the file with repeats:

|track|artist|album|date|count|
|:---:|:----:|:---:|:---:|:---:|
|Spare Time|Shortly|Spare Time|9/20/2018|6|
|Revisited|The Antlers|Familiars|9/20/2018|5|
|Mary|Big Thief|Capacity|9/19/2018|8|
|Shark Smile|Big Thief|Capacity|9/19/2018|35|
|Don't Stay Here / Gun Nut|The Album Leaf|The Endless (Original Motion Picture Soundtrack)|9/18/2018|24|

and here without repeats:

|track|artist|album|date|count|
|:---:|:----:|:---:|:---:|:---:|
|Spare Time|Shortly|Spare Time|9/20/2018|6|
|Revisited|The Antlers|Familiars|9/20/2018|5|
|Shark Smile|Big Thief|Capacity|9/19/2018|5|
|Don't Stay Here / Gun Nut|The Album Leaf|The Endless (Original Motion Picture Soundtrack)|9/18/2018|24|
|Deep Snow|Grails|Deep Politics|9/17/2018|8|

Needless to say, I've been listening on repeat a lot recently.

## [lastfm_data.py](https://github.com/becca-miller/lastfm-music/blob/master/lastfm_data.py)

This script is used to download listening history from a user account at Last.fm. Note that to use this file, you will need to get a Last.fm [API key](https://www.last.fm/api). Alternatively, the output using my account is stored at [listening_history.csv](https://github.com/becca-miller/lastfm-music/blob/master/data/listening_history.csv) and can be used for other scripts.
