#!/bin/python3
##################################
# LED stuff
# from gpiozero import LED
# import time
# led = LED(2)
# led.on()
# time.sleep(1)
##################################

# stepper motor stuff
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
coil_A_1_pin = 17
coil_A_2_pin = 18
coil_B_1_pin = 27
coil_B_2_pin = 22

# Setup pins
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Full-step sequence
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def forward(delay, steps):
    for i in range(steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)

# Main loop
try:
    while True:
        # 0.002s is a good starting delay for 28BYJ-48
        forward(int(2) / 1000.0, 500) 
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
