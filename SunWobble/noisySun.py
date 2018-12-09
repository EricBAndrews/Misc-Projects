# THE BELOW CODE IS BASED ON https://www.daniweb.com/programming/software-development/code/217024/creating-and-playing-a-sine-wave-sound-python

import numpy as np
from struct import pack
from math import sin, pi

def wave(x):
    val = (
    .00808 * (sin((2 * pi / 87.97)  * (x))) + # Mercury
    .08711 * (sin((2 * pi / 224.71) * (x))) + # Venus
    .09091 * (sin((2 * pi / 365.26) * (x))) + # Earth
    .00791 * (sin((2 * pi / 686.99) * (x))) + # Mars
    12.673 * (sin((2 * pi / 4332.9) * (x))) + # Jupiter
    2.8017 * (sin((2 * pi / 10756)  * (x))) + # Saturn
    .30107 * (sin((2 * pi / 30688)  * (x))) + # Uranus
    .28539 * (sin((2 * pi / 60192)  * (x))) + # Neptune
    .00003 * (sin((2 * pi / 90592)  * (x)))   # Pluto
        )
    return val / 16.2552

def au_file(name, freq, dur, vol):
    """
    creates an AU format audio file of a sine wave
    of frequency freq (Hz)
    for duration dur (milliseconds)
    at volume vol (max is 1.0)
    """
    fout = open(name, 'wb')
    # header needs size, encoding=2, sampling_rate=8000, channel=1
    fout.write('.snd' + pack('>5L', 24, 8*dur, 2, 8000, 1.0))
    factor = float(freq)
    # write data
    max = 0
    min = 0
    for seg in range(8 * dur):
        # sine wave calculations
        sin_seg = wave(seg * factor)
        if (sin_seg > max):
            max = sin_seg
        if (sin_seg < min):
            min = sin_seg
        fout.write(pack('b', vol * 127 * sin_seg))
    print(max, min)
    fout.close()
    
# test the module ...
if __name__ == '__main__':
    for i in range(8):
        freq = 2**i
        print(freq)
        name = 'sounds/sun' + str(freq) + '.au'
        au_file(name, freq, dur=4000, vol=1.0)

    # if you have Windows, you can test the audio file
    # otherwise comment this code out
    # import os
    # os.startfile('sound800.au')
