import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
button = 13
GPIO.setup(6, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

state = 0
period = 1.5

while True:
    state = GPIO.input(6)
    GPIO.output(led, state)
    time.sleep(0.2)

