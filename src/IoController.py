# -*- coding: utf-8 -*-
try:
    import RPi.GPIO as GPIO
except:
    print("Fehler beim Import von RPi")
import time


def initIO():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(17, GPIO.OUT)
    #GPIO.output(17, GPIO.LOW)
    print("initialisierung...")

def bootPC():


    #GPIO.output(17, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(17, GPIO.LOW)
    print("Tasten druck")
    time.sleep(1)
    print("Taste loslassen")
