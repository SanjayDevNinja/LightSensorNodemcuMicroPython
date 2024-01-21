import paho.mqtt.client as mqtt

from tkinter import *
from tkinter.ttk import *
from threading import Thread

# this is the subscriber
broker_address="192.168.137.1"
topic = 'LightLevel'

LightReadings = [500]

def on_connect(client, userdata, flags, rc) :
    print("connected with result code"+str(rc))
    
def on_message(client, userdata, msg):
   reading = int(msg.payload.decode())
   print(reading)
   DisplayCurrentReading['text'] = "Current Reading: " + msg.payload.decode()
   plotLightReadings(reading)
        
def startSubcription():
    
    client = mqtt.Client()
    client.connect(broker_address,1883)

    client.subscribe(topic)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()  



def threadFunct():
     t1 = Thread(
            daemon=True,
            target=startSubcription             #name of he method to run as a thread
        )
     
     StartBtn['state'] = DISABLED
     t1.start()                      #starts the thread    

def plotLightReadings(reading):
    number_of_values = 250
    #canvas_plot.create_line(y, width=3)
    canvas_plot.delete('all')
    #y.pop(0)
    #shift values
    LightReadings.append(reading/2)
    if len(LightReadings) > number_of_values:
        LightReadings.pop(0)


    plot = [(x*4, LightReadings[x]) for x in range(len(LightReadings))]
    #y.clear()
    #y.extend(z)    
    #y.append((len(y)*2,((500-TempSensor1.generateTemp()-480)*400)))    
    canvas_plot.create_line(plot, width=2)   

###################Tkinter GUI##################
root = Tk()   

StartBtn = Button(
root,
command=threadFunct,
text='Start Reading Light Sensor', # the text to go on this widget
state=NORMAL # the NORMAL is the default
)
StartBtn.pack()

Label(
root, # the host container
text='Light Readings', # the text to go on this widget
).pack()

CurrentLightReading = StringVar() #variable that will be used to communicate
DisplayCurrentReading = Label( #creates an Entry
root, #parent
text='Current Reading: '
)
DisplayCurrentReading.pack()

canvas_plot = Canvas(root,  bg='lightgray', height=500, width=1000)
canvas_plot.pack()

root.mainloop()

  
