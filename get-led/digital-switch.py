import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 18
button = 13

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

state = False
GPIO.output(led, state)

try:
    while True:
        if GPIO.input(button):
            state = not state
            GPIO.output(led, state)
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()