#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

INT = 3

GPIO.setup(INT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    while True:
        GPIO.wait_for_edge(INT, GPIO.FALLING)
        sleep(5)

        if GPIO.input(INT) == 0:
            subprocess.call(['shutdown', '-h', 'now'], shell=False)

if __name__ == '__main__':
    main()
