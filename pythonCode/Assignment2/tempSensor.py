import matplotlib.pyplot as plt
import random

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


