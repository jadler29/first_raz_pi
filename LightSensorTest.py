import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIGHT_PIN = 11
GPIO.setup(LIGHT_PIN, GPIO.IN)
lOld = not GPIO.input(LIGHT_PIN)
print('Starting up the LIGHT Module (click on STOP to exit)')
time.sleep(0.5)
while True:
  if GPIO.input(LIGHT_PIN) != lOld:
    if GPIO.input(LIGHT_PIN):
      print ('\u263e')
    else:
      print ('\u263c') 
  lOld = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)
