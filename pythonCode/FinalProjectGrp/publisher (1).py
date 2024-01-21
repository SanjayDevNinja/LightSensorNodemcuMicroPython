import paho.mqtt.client as mqtt
import time
broker_address="192.168.137.1"
#mqtt.eclipseprojects.io
#broker_address ="192.168.1.102"

# this is the publisher

client = mqtt.Client("p1")
client.connect(broker_address,1883)
client.loop_start()
client.publish("test","Hello world")
client.disconnect()
client.loop_stop()