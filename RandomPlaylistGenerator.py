import os
import random
from random import choice
import re

#Enter your music directory here:
directory = "C:/Users/osaid/songs"
#Enter your music player's directory
music_player = "C:/Program Files (x86)/MusicBee/MusicBee.exe"


music_list = []
parent_files = []
for filename in os.scandir(directory):
            parent_files.append(filename.path)

print("Enter the size of the playlist(number of songs) :")
num = input("Type here:")
num = int(num)

for counter, i in enumerate(parent_files):
	print(counter, ": ",i)

print("Enter the artists that you want to add (indexes), comma seperated")
print("Enter 'all' if you have no preference")
artists_selection = input("Type here:")

if (artists_selection == "all"):
    artists_selection = []
    for counter, i in enumerate(parent_files):
        artists_selection.append(str(counter))
else:
    artists_selection = artists_selection.split(",")

random.shuffle(artists_selection)

new_parent_files = []
for counter, i in enumerate(parent_files):
    if str(counter) in artists_selection:
        new_parent_files.append(i)
        
for i in new_parent_files:
    for files in os.scandir(i):
        if files.is_file():
            if files.name.endswith('.mp3'):
                    random.shuffle(music_list)
                    music_list.append(files.path)
                    

        if files.is_dir():
            for k in os.scandir(files):
                if k.is_file():
                    if k.name.endswith('.mp3'):
                        random.shuffle(music_list)
                        music_list.append(k.path)


for i in range(0,10):
    random.shuffle(music_list)

new_music_list = []
total_songs = 0
for songs in music_list:
    if total_songs > int(num):
        break
    total_songs = total_songs + 1
    new_music_list.append(songs)


import subprocess
music_player = music_player.replace("/","\\")
l1 = list()
l1.append(music_player)
for m in new_music_list:
    m = m.replace("/","\\")
    l1.append(m)
subprocess.Popen(l1)
