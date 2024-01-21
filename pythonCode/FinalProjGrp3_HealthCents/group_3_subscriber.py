import paho.mqtt.client as mqtt

from tkinter import *
from tkinter.ttk import *
from threading import Thread

# this is the subscriber
## broker_address="192.168.137.1"
#broker_address= "mqtt.eclipseprojects.io"
broker_address= "localhost"
topic = 'heartRate'

LightReadings = [500]

client1 = mqtt.Client()
client2 = mqtt.Client()
    
def on_message(client, userdata, msg):
   reading = eval(msg.payload.decode())
   print("Heart Rate Package:",reading)
   DisplayCurrentReading['text'] = "Current Reading: " + str(reading["heartRate"])
   plotLightReadings(reading["heartRate"])


def startSubcription():
    global client1
    client1 = mqtt.Client()
    client1.connect(broker_address)
    client1.subscribe(topic)
    client1.on_message = on_message
    client1.loop_forever()  

def threadFunct():
     global t1
     t1 = Thread(
            daemon=True,
            target=startSubcription             #name of he method to run as a thread
        )
     heartRateLabel["bg"] = "red"
     StartBtn['state'] = DISABLED
     StartBtn2['state'] = DISABLED
     t1.start()                      #starts the thread    

##For Blood Pressure--------------------------------------------
def startSubcription2():
    global client2
    client2 = mqtt.Client()
    client2.connect(broker_address)
    client2.subscribe("BloodPressure")
    client2.on_message = on_message2
    client2.loop_forever()  

def threadFunct2():
     global t2
     t2 = Thread(
            daemon=True,
            target=startSubcription2             #name of he method to run as a thread
        )
     
     bloodPressureLabel["bg"] = "red"
    
     StartBtn['state'] = DISABLED
     StartBtn2['state'] = DISABLED
     t2.start()                      #starts the thread    

def on_message2(client, userdata, msg):
   reading = eval(msg.payload.decode())
   print("Blood Pressure Package:",reading)
   DisplayCurrentReading2['text'] = "Current Reading: " + str(reading["bloodPressure"])
   plotLightReadings(reading["bloodPressure"])

##End Blood Pressure--------------------------------------------

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

def stopReadings():
    global client1
    global client2
    global LightReadings
    client1.disconnect()
    client2.disconnect()
    StartBtn['state'] = NORMAL
    StartBtn2['state'] = NORMAL
    LightReadings.clear()
    LightReadings = [500]
    canvas_plot.delete('all')
    bloodPressureLabel["bg"] = "white"
    heartRateLabel["bg"] = "white"



###################Tkinter GUI##################
from tkinter import *
from pathlib import Path
root  =  Tk()  # create root window
root.title("Patient Health Monitoring")
root.maxsize(900,  600)
root.config(bg="lightgrey")

#Heart Rate------------------------------------------------------------------
left_frame  =  Frame(root,   bg='white')
left_frame.pack(side='top',  fill='both',   padx=10,  pady=5,  expand=True)

script_dir = Path(__file__).parent.absolute()
resource_path = script_dir / "1.png"

Label(left_frame,  text="Heart Rate / Blood Pressure").pack(side='top',  padx=5,  pady=5)
image = PhotoImage(file=str(resource_path))
original_image = image.subsample(2,7)  # resize image using subsample
Label(left_frame,  image=original_image).pack(fill='both',  padx=5,  pady=5)

tool_bar  =  Frame(left_frame,  width=500,  bg='lightgrey')
tool_bar.pack(side='left',  fill='both',  padx=5,  pady=5,  expand=True)

StartBtn = Button(
tool_bar,
command=threadFunct,
text='Start Reading Heart Rate', # the text to go on this widget
state=NORMAL # the NORMAL is the default
)
StartBtn.pack(padx=5,  pady=5)

heartRateLabel = Label(
tool_bar, # the host container
text='Heart Rate Readings', # the text to go on this widget
)
heartRateLabel.pack(anchor='n',  padx=5,  pady=3,  ipadx=10)

CurrentLightReading = StringVar() #variable that will be used to communicate
DisplayCurrentReading = Label( #creates an Entry
tool_bar, #parent
text='Current Reading: '
)
DisplayCurrentReading.pack()

#Blood Pressure----------------------------------------------------------------------
filter_bar  =  Frame(left_frame,  width=500,  height=185,  bg='lightgrey')
filter_bar.pack(side=RIGHT,  fill='both',  padx=5,  pady=5,  expand=True)
StartBtn2 = Button(
filter_bar,
command=threadFunct2,
text='Start Reading Blood Pressure', # the text to go on this widget
state=NORMAL # the NORMAL is the default
)
StartBtn2.pack(padx=5,  pady=5)

bloodPressureLabel = Label(
filter_bar, # the host container

text='Blood Pressure Readings', # the text to go on this widget
)
bloodPressureLabel.pack(anchor='n',  padx=5,  pady=3,  ipadx=10)

CurrentLightReading2 = StringVar() #variable that will be used to communicate
DisplayCurrentReading2 = Label( #creates an Entry
filter_bar, #parent
text='Current Reading: '
)
DisplayCurrentReading2.pack()


StopBtn = Button(
root,
command=stopReadings,
text='Stop Readings', # the text to go on this widget
state=NORMAL # the NORMAL is the default
)
StopBtn.pack(padx=5,  pady=5)


#canvas
canvas_plot = Canvas(root,  bg='lightgray', height=500, width=1000)
canvas_plot.pack(side='bottom',  fill='both',  padx=10,  pady=5,  expand=True)


root.mainloop()