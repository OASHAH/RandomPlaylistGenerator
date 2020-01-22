import os
import random
from random import choice
import re

#Enter your music directory here:
directory = "C:/Users/osaid/songs"
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

'''
import vlc
p = vlc.MediaPlayer(new_music_list[0])
p.play()
'''
import pygame
import random
import time
pygame.mixer.init(44100, -16,2,2048)
templist = new_music_list.copy()
temp = templist[-1]
new_music_list[1:] = new_music_list[0:-1]
new_music_list[0] = temp

for counter, m in enumerate(new_music_list):
    print(counter)
    if (counter == 0):
        pygame.mixer.music.load(m)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.queue(m)

            
