import RPi.GPIO as GPIO
import time

# use BCM or BOARD, but note that they have different pin layouts
GPIO.setmode(GPIO.BOARD)

# this is our pin on the rpi that connects to the relay
relayPin = 3

# this is how long the relay stays on
sleepDuration = 5

# setting up gpio pin
GPIO.setup(relayPin, GPIO.OUT)
GPIO.output(relayPin, GPIO.HIGH)

try:
	# turn on the relay
	GPIO.output(relayPin, GPIO.LOW)
	print "Turning Relay ON"
	# sleep
	time.sleep(sleepDuration)
	# turn off the relay
	GPIO.output(relayPin, GPIO.HIGH)
	print "Turning Relay OFF"

	# reset gpio pin
	GPIO.cleanup()

except KeyboardInterrupt:
	print " Quit"

	# reset gpio pin
	GPIO.cleanup()






