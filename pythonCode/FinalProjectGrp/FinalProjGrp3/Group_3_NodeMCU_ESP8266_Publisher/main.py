from machine import Pin,ADC
from time import sleep


print('main excuting')

#light sensor connected to Analog pin 0
adc = ADC(0)
HighValueLED = Pin(4, Pin.OUT)
LowValueLED = Pin(5, Pin.OUT)

HighValueLED.value(0)
LowValueLED.value(0)

client = MQTTClient(client_id, mqtt_server,keepalive=10)
client.connect()



start = time.ticks_ms()
seconds = 0
while True: #seconds < 30000:
    seconds = time.ticks_ms()-start
    
    lightReading = adc.read()
    print(lightReading)
    
    if lightReading > 700 :
        HighValueLED.value(1)
    else:
        HighValueLED.value(0)
    
    if lightReading < 120 :
        LowValueLED.value(1)
    else:
        LowValueLED.value(0)
    
    client.publish(topic, str(lightReading))
    sleep(1)
