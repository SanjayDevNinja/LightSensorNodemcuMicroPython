import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import datetime

#Import Custom random generator
import ValueGenerator as sensor

## this is the mqttBroker
#broker_address="mqtt.eclipseprojects.io"
broker_address="localhost"

client = mqtt.Client("HeartRate")
client.connect(broker_address,1883) ## connect client to the broker

#Simulate sensor with desired parameter values
HeartRateSensor = sensor.ValueGenerator(minVal=60.0,maxVal=150.0,spread=0.2)

while True:    
    heartRate = HeartRateSensor.generateVal()

    package = {"timeStamp": str(datetime.datetime.now()), "heartRate": heartRate}
    
    client.publish("heartRate", str(package))
    #randfloat = round(randNumber, 4)
    print("Just published " + str(heartRate) + " to Topic Heart Rate")
    time.sleep(1)


