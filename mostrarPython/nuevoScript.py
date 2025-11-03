import vlc
import time

files = ['./../data/085.mp4', './../data/097.mp4'] 
instances = []
medias = []
players = []



for idx, fname in enumerate(files):
    print("Loading", fname)
    instances.append(vlc.Instance())
    medias.append(instances[idx].media_new(fname))

    players.append(vlc.MediaPlayer())
    players[idx].set_media(medias[idx])
    players[idx].play() 


# copy of the players list so we don't modify during iteration
player_count = players
still_playing = True
# Wait for players to start
time.sleep(0.5) 

while still_playing:
    time.sleep(1)
    for p in players:
        if p.is_playing():
            continue
        else:
            player_count.remove(p)
            # no point iterating over players that have finished
            players = player_count 
            print("Finished - Still playing ", str(len(player_count)))

    if len(player_count) != 0:
        continue
    else:
        still_playing = False
