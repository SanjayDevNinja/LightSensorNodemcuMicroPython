import matplotlib.pyplot as plt
import random


from tkinter import *
from tkinter.ttk import *

from time import sleep
from threading import Thread

#import tempSensor
##########################################################################################
class TempSensor:
    '''
    Emulates a temperature sensor 
    to generate sensor data values
    ranging from 18-21 deg Celcius
    '''

    #class variable to maintain peak data
    __value = {

    }

    #maxTemp, minTemp, variation,
    def __init__(self, maxTemp=21, minTemp=18, base=0.5, spread=0.1, delta= 0.005, minCycle=2, maxCycle=10) -> None:        
        self.maxTemp = maxTemp
        self.minTemp = minTemp        
        self.maxCycle = maxCycle
        self.minCycle = minCycle
        self.spread = spread
        TempSensor.__value['base'] = base        
        TempSensor.__value['delta'] = delta
        TempSensor.__value['cycle'] = maxCycle


    #Requirement 1: generate random values in the range 0-1
    #def __genRand() -> float:       
    #    return random.random()
    
    def generator_2(min, max) -> int:
        '''
        This generator gives you a uniform random number in min max range
        '''
        return random.randint(min, max)
    
    def generator_3(base, spread) -> int:
        return random.gauss(base, spread)
    
    def generator_4(self) -> float:
        TempSensor.__value['cycle'] -= 1  #decrease cycle 
        if TempSensor.__value['cycle'] == 0: #end of cycle
            TempSensor.__value['cycle'] = TempSensor.generator_2(self.minCycle, self.maxCycle) #new length the randomize
            TempSensor.__value['delta'] *= -1                   #flip the incrementer

        TempSensor.__value['base'] +=  TempSensor.__value['delta']
        return TempSensor.__value['base'] + TempSensor.generator_2(-5, 5)/500 #Squiggles


    def generateFinal(self):
        return self.generator_4()

    #Requirement 2: Transpose random values to desired range
    def generateTemp(self) -> float:
        m = self.maxTemp - self.minTemp
        x = self.generateFinal()
        c = self.minTemp
        #y = mx + c
        y = m*x + c       
        
        return y



TempSensor1 = TempSensor()
number_of_values = 500
#scale value to fit as best on the canvas
y = [(x*2,(500-TempSensor1.generateTemp()-480)*400) for x in range(number_of_values)]
#print(y)
########################################################################################################################

def threadFunct():
     t1 = Thread(
            daemon=True,
            target=plotTemp             #name of he method to run as a thread
        )
        
     t1.start()                      #starts the thread

def plotTemp():

    while True:         
        #canvas_plot.create_line(y, width=3)
        canvas_plot.delete('all')
        #y.pop(0)
        #shift values
        z = [(x*2, y[x+1][1]) for x in range(number_of_values - 1)]
        y.clear()
        y.extend(z)    
        y.append((len(y)*2,((500-TempSensor1.generateTemp()-480)*400)))    
        canvas_plot.create_line(y, width=3)
        sleep(0.5)
    



root = Tk()

Button(
root,
command=threadFunct,
text='Start', # the text to go on this widget
state=NORMAL # the NORMAL is the default
).pack()

Label(
root, # the host container
text='Temperature', # the text to go on this widget
).pack()

canvas_plot = Canvas(root,  bg='lightgray', height=500, width=1000)
canvas_plot.pack()

root.mainloop()