import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# this is our pin on the rpi that connects to the relay
relayPin = 3

GPIO.setup(relayPin, GPIO.OUT)
GPIO.output(relayPin, GPIO.HIGH)

