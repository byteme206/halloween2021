#!/usr/bin/env python3


import os.path
from phue import Bridge


if (os.path.isfile('phue.ini')):
    with open('phue.ini', 'r') as f:
        bridgeip = f.read()
        f.close()
else:
    bridgeip = input('Enter the Hue bridge IP address: '')
    bem = input('OK, go press the Push-Link button on your hub and then press ENTER.'')
    b = Bridge(bridgeip)

    print('Attempting Hue bridge connection...')

    try:
        b.connect()
        tf = open('phue.ini', 'w')
        n = tf.write('{0}'.format(bridgeip))
        tf.close()
        print('Checking bridge status...')
        print(b.get_api())
    except Exception as e:
        raise
        exit(127)
