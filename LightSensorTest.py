import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

camera = PiCamera()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LIGHT_PIN = 11
GPIO.setup(LIGHT_PIN, GPIO.IN)
lOld = not GPIO.input(LIGHT_PIN)
print('Starting up the LIGHT Module (click on STOP to exit)')
time.sleep(0.5)

while True:
  if GPIO.input(LIGHT_PIN) != lOld:
    if GPIO.input(LIGHT_PIN):
      print ('Dark/0v')
    else:
      print ('Light/5v')
      camera.capture('LightPic2.jpg')
  lOld = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)
