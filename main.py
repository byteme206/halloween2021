#!/usr/bin/env python3


import random
import serial
from pathlib import Path
from time import sleep
from omxplayer.player import OMXPlayer
from phue import Bridge


B_USB = '/dev/ttyACM0'
C_USB = '/dev/ttyACM1'

vidargs = [
    '--no-osd',
    '--no-keys',
    '-b'
]

media_files = [
    './media/loop.mp4',
    './media/wakey.mp4',
    './media/intro.mp4',
    './media/bicker.mp4',
    './media/dadjokes.mp4',
    './media/candy.mp4',
]




def mplay(strpath):
    MEDIA_PATH = Path(strpath)
    player = OMXPlayer(MEDIA_PATH, args=vidargs)
    player.play()
    player.quit()


def ravelites(time):
    pass

# Initialize USB connection to the two nask props
try:
    bili = serial.Serial(B_USB, 115200, timeout=2)
except Exception as e:
    print('Could not open USB connection to Bilious mask.')
    exit()

try:
    cank = serial.Serial(C_USB, 115200, timeout=2)
except Exception as e:
    print('Could not open USB connection to Cankerous mask.')
    exit()

# Initialize connection to the Hue bridge
if (os.path.isfile('phue.ini')):
    with open('phue.ini', 'r') as f:
        bridgeip = f.read()
        b = Bridge(bridgeip)
        f.close()

    try:
        b.connect()
    except Exception as e:
        print('Couldn not connect to the Hue bridge.')
        exit()


# Main loop
while True:
    pass
