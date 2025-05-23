import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(21, GPIO.OUT)

print("Drücke den Taster (STRG+C zum Beenden)")
try:
    while True:
        if GPIO.input(26) == False:
            GPIO.output(21, True)  
            print("Taster gedrückt – Aus")
        else:
            GPIO.output(21,False)  
            print("Taster nicht gedrückt – An")
        time.sleep(0.1)

    print("Beendet")
finally:
    GPIO.cleanup(26)

