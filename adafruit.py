
import time
import Adafruit_DHT

DHT_PIN = 22
DHT_TYPE = Adafruit_DHT.DHT11

try:
    while True:
        hum, temp = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
        
        #print('{0:0}, {1,0}'.format(temp,hum))
        
       
        if hum is not None and temp is not None:
            print('Temp = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temp,hum))
        else:
            print('Failed to get reading. Try again!')
       

except KeyboardInterrupt:
    print("^C pressed")
