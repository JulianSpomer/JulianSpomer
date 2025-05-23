import RPi.GPIO as GPIO 
import time
import 
GPIO.setmode (GPIO.BCM)
GPIO.setup (21, GPIO.OUT)
GPIO.setwarnings(False)
while True:
  GPIO.output(21, True)
  time.sleep(0.1)
  GPIO.output(21, False)
  time.sleep(0.1)
  GPIO.setup(26, GPIO.IN)
  print (GPIO.input(26))
  GPIO.output(21, True)




