import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import *
# Define the function prefixes using NumPy
class Numerical_Integration:
    # The a , b  , F --> function self --> is the object its self 
    def __init__(self, F, a, b):
        self.Function = F
        self.a = a
        self.b = b
        self.StepSize = b - a # b-a le pas h
# Define the function prefixes using NumPy

    def f(self, x):
        return eval(self.Function, {'x': x, 'np': np})
        
    
    def TrapeziodalRule(self): #---> Trapezoidal Rule
        I=(1/2)*(self.StepSize)*(self.f(self.a)+self.f(self.b))
        return I
    
    def SimpsonRule(self): #---> Simpson's  Rule
        I=(1/6)*(self.StepSize)*(self.f(self.a)+4*self.f((self.a+self.b)/2)+self.f(self.b))
        return I
    
    
    
    
    
    def __str__(self):
        Result={"Trapezoidal Rule            |": str(self.TrapeziodalRule()),
                "Simpson's Rule                  |": str(self.SimpsonRule())}
        
        Table = pd.DataFrame({'Results ': Result})
    
        return f"{Table}"
    
    def Graph(self):
        xAxisPoints=np.linspace(floor(self.a),ceil(self.b),10000)
        yAxisPoints=self.f(xAxisPoints)
        ax = plt.gca()
        section = np.arange(self.a,self.b, 1/1000.)
        ax.plot(xAxisPoints, yAxisPoints)
        plt.style.use('ggplot')
        plt.title('Graph Representation')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.fill_between(section,self.f(section),color="cyan")
        plt.show()

if __name__=='__main__':
    Function=input("F(X) =  ")
    a=float(input(" (a) = "))
    b=float(input(" (b) = "))
    Calc = Numerical_Integration(Function, a, b)
    print(Calc)
    Calc.Graph()
    

    # Ex01 : You can use this input : np.exp(-x**2) for e(-x^2)
    # And the Same for other function such (sin,cos,log,log10,tan...)