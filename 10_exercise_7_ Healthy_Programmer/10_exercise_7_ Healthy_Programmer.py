# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log 30 min
# Physical activity - physical.mp3 every - log 45 min
#
# Rules
# Pygame module to play audio

import pygame
from pygame import mixer
from datetime import datetime
from time import time

def music_play(music_file,stoping_word):
    mixer.init()
    sounda = mixer.Sound(music_file)
    sounda.play(-1)
    while True:
        user_word=input()
        if user_word==stoping_word:
            sounda.stop()
            break
num=0
def log(message):

    with open("mylogs.txt", "a") as file1:
        file1.write(f"{num}) [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] : {message}\n")
    print("your time has been recorded")


systime_water=time()
systime_eyes=time()
systime_physical=time()

water=40*60 # 40 minutes -> 40*60sec
eyes=30*60 # 30 minutes -> 30*60sec
physical=45*60 # 45 minutes -> 45*60sec

while True:
    if time() - systime_water > water:
        num+=1
        print("water drinking time.enter done to stop alarm")
        music_play("water.mp3","done")
        log("Drank water")
        systime_water=time()

    if time()-systime_eyes> eyes:
        num += 1
        print("eyes exercise time.enter done to stop alaram")
        music_play("eyes.mp3","done")
        log("exercise done")
        systime_eyes=time()

    if time()-systime_physical>physical:
        num += 1
        print("physical activity time.enter done to stop alaram")
        music_play("physical.mp3","done")
        log("physical activity done")
        systime_physical=time()
