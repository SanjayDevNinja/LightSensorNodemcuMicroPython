import random

class ValueGenerator:
    '''
    Emulates a sensor 
    to generate sensor data values    
    '''

    #class variable to maintain peak data
    __value = {

    }

    #maxVal, minVal, variation,
    def __init__(self, maxVal=21, minVal=18, base=0.5, spread=0.1, delta= 0.005, minCycle=2, maxCycle=10) -> None:        
        self.maxVal = maxVal
        self.minVal = minVal        
        self.maxCycle = maxCycle
        self.minCycle = minCycle
        self.spread = spread
        ValueGenerator.__value['base'] = base        
        ValueGenerator.__value['delta'] = delta
        ValueGenerator.__value['cycle'] = maxCycle


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
        ValueGenerator.__value['cycle'] -= 1  #decrease cycle 
        if ValueGenerator.__value['cycle'] == 0: #end of cycle
            ValueGenerator.__value['cycle'] = ValueGenerator.generator_2(self.minCycle, self.maxCycle) #new length the randomize
            ValueGenerator.__value['delta'] *= -1                   #flip the incrementer

        ValueGenerator.__value['base'] +=  ValueGenerator.__value['delta']
        return ValueGenerator.__value['base'] + ValueGenerator.generator_2(-5, 5)/500 #Squiggles


    def generateFinal(self):
        return self.generator_4()

    #Requirement 2: Transpose random values to desired range
    def generateVal(self) -> float:
        m = self.maxVal - self.minVal
        x = self.generateFinal()
        c = self.minVal
        #y = mx + c
        y = m*x + c       
        
        return y


