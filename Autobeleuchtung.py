import RPi.GPIO as GPIO
import dht11
import time
global press_time

# Benutzte GPIOs freigeben
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(13, GPIO.IN)
sensor = dht11.DHT11(pin=23) #pin 23 als sensor setzten

sensorpin = 23
press_time = 0


try:
    while True:
        result = sensor.read()
        # Abfragen des Wertes des Tasters
        press_time = time.time()
        
       
        if result.is_valid():
            temperature = result.temperature #speichert die Temperature
            humidity = result.humidity #speichert die Luftfeuchtigkeit
            print(f"Temp: {temperature}°C, Humidity: {humidity}%") #printet die Temperatur und Luftfeuchtigkeit
            time.sleep(0.2)
            
            if result.temperature >= 25:
                #Lüftung LED an
                print("LED ON")
                GPIO.output(24,GPIO.HIGH)   

            else :
                #Lüftung LED aus
                print("LED OFF")
                GPIO.output(24, GPIO.LOW)
                
        
        
        elif GPIO.input(26) == GPIO.HIGH:
            # LED deaktivieren
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
            
        
        elif durationO < 0.5:
            
            durationO = time.time() - press_time
            print("kurz")
        
        
        elif GPIO.input(5) == GPIO.HIGH:
            #Blinker oben
            GPIO.output(21, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(21, GPIO.LOW)
            time.sleep(0.5)

        elif GPIO.input(13) == GPIO.HIGH:
            #Blinker unten
            GPIO.output(19, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(19, GPIO.LOW)
            time.sleep(0.5)

        else:
            # LED aktivieren
            GPIO.output(6, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(21, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            
        
    
            


        # Eine kleine Pause von 100 Millisekunden
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programm beendet.")

finally:
    GPIO.cleanup()