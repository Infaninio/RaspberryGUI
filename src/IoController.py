# -*- coding: utf-8 -*-
try:
    import RPi.GPIO as GPIO
except:
    print("Fehler beim Import von RPi")
import time
import platform
import os


def initIO():
    if "Win" in platform.platform():
        print("Windows, IO initialisiert")
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    print("initialisierung...")

def bootPC():
    if "Win" in platform.platform():
        print("Windows, Start PC")
        return

    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    print("Tasten druck")
    time.sleep(1)
    print("Taste loslassen")


def avReceiver():
    os.system("irsend SEND_ONCE denon KEY_POWER")

def avPc():
    os.system("irsend SEND_ONCE denon KEY_COMPUTER")

def avRpi():
    os.system("irsend SEND_ONCE denon KEY_BLUE")

def avBlp():
    os.system("irsend SEND_ONCE denon KEY_DVD")

def avMode():
    os.system("irsend SEND_ONCE denon KEY_MODE")

def beamerPwr():
    os.system("irsend SEND_START beamer KEY_POWER")
    time.sleep(2)
    os.system("irsend SEND_STOP beamer KEY_POWER")