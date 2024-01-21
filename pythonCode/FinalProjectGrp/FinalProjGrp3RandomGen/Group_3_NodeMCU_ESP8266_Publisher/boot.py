# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
####import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
####import gc
#import webrepl
#webrepl.start()
####gc.collect()

# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
print("Trying to connect now")
ssid = "laptoplocal"
password = 'sanjay1234'

mqtt_server = '192.168.137.1'
client_id = 'LightSensor'#ubinascii.hexlify(machine.unique_id())
topic = 'LightLevel'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

#timeout for connecting to wifi
OnboardLed = machine.Pin(16, machine.Pin.OUT)
OnboardLed.value(0) #led is on, 0 is on for onboard led
start = time.ticks_ms()
seconds = 0
wifi_connected = True
while station.isconnected() == False:
    seconds = time.ticks_ms()-start
    if seconds > 15000 : #15 seconds
        print('Failed to connect to Wifi')
        wifi_connected = False
        OnboardLed.value(1)
        break    


if wifi_connected :
    print('Connection successful')
    print(station.ifconfig())





