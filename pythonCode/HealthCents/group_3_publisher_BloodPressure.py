import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import datetime

#Import Custom random generator
import ValueGenerator as sensor

## this is the mqttBroker
#broker_address="mqtt.eclipseprojects.io"
broker_address="localhost"

client = mqtt.Client("BloodPressure")
client.connect(broker_address,1883) ## connect client to the broker

#Simulate sensor with desired parameter values
BloodPressureSensor = sensor.ValueGenerator(minVal=90.0,maxVal=150.0,spread=0.1)

while True:    
    bloodPressure = BloodPressureSensor.generateVal()

    package = {"timeStamp": str(datetime.datetime.now()), "bloodPressure": bloodPressure}
    
    client.publish("BloodPressure", str(package))
    #randfloat = round(randNumber, 4)
    print("Just published " + str(bloodPressure) + " to Topic Blood Pressure")
    time.sleep(1)


