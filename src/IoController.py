# -*- coding: utf-8 -*-
try:
    import RPi.GPIO as GPIO
except:
    print("Fehler beim Import von RPi")
import time
import platform
import os

A = 26
B = 19
C = 13
D = 6

def initIO():
    if "Win" in platform.platform():
        print("Windows, IO initialisiert")
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)

    #Initialize for StepperEngine
    GPIO.setup(A, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    GPIO.setup(C, GPIO.OUT)
    GPIO.setup(D, GPIO.OUT)


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


def stepperStep(a, b, c, d):
    GPIO.OUTPUT(A, a)
    GPIO.OUTPUT(B, b)
    GPIO.OUTPUT(C, c)
    GPIO.OUTPUT(D, d)
    time.sleep(0.0001)

def scUP():
    stepperStep(0,0,0,0)

    for i in range(0,1000):
        for i in range(0,100):
            stepperStep(1,0,0,0)
            stepperStep(1,1,0,0)
            stepperStep(0,1,0,0)
            stepperStep(0,1,1,0)
            stepperStep(0,0,1,0)
            stepperStep(0,0,1,1)
            stepperStep(0,0,0,1)
            stepperStep(1,0,0,1)

    stepperStep(0,0,0,0)

def scDOWN():
    stepperStep(0,0,0,0)

    for i in range(0,1000):
        for i in range(0,100):
            stepperStep(1,0,0,1)
            stepperStep(0,0,0,1)
            stepperStep(0,0,1,1)
            stepperStep(0,0,1,0)
            stepperStep(0,1,1,0)
            stepperStep(0,1,0,0)
            stepperStep(1,1,0,0)
            stepperStep(1,0,0,0)

    stepperStep(0,0,0,0)