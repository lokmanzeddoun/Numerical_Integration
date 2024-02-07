
import numpy as np
import Simpson_Traperzoid as St   # If you Want to Use Jupyter Note Book YOu delete This line
# Define the function prefixes using NumPy
sin = np.sin
cos = np.cos
tan = np.tan
pi  = np.pi
exp = np.exp
ln  = np.log
log = np.log10
# Part 1
# Trapezoid method
#*******************************************************************
def Trapezoid_Composite(g, a, b, n):
    f = lambda x: eval(g)    # define function to evaluate
    
    h = float((b - a) / n)  
    s1 = 0
    for i in range(1, n, 1):
        s1 = s1 + 2 * f(a + i * h)


    # defining the area
    area = (h / 2) * (f(a) + f(b) + s1 )

    print('Trapezoid Composite Integral =', area)
        
    
#*******************************************************************    


# Part 2
# Simpson method
#*******************************************************************
def Simpson_Composite(g, a, b, n):
    f = lambda x: eval(g)  # define function to evaluate
    h = float((b - a) / n)  # interval size (using n rather than n-1 for Python)
    s1 = 0
    s2 = 0
    for i in range(1, n, 1):
        s1 = s1 + 2 * f(a + i * h)

    for i in range(1, (n + 1), 1):
        s2 = s2 + 4 * f(a + (i - 0.5) * h)

    # defining the area
    area = (h / 6) * (f(a) + f(b) + s1 + s2)

    print('Simpson Composite Integral =', area)



        
#we can continue the Ex01 : of the function (exp(-x**2)): by passing the parameters ("exp(-x**2)",3,0,0.5)
#------------------------------------------------------------------- 
#*******************************************************************
    
if __name__=='__main__':
    # take function as input from the user
    fx = input("Enter the function whose integral you wish to determine : ")    

    # Enter the iterations and limits of integration
    r = int(input('Enter the number of sub-intervals : '))

    a = float(input('Please provide the lower limit (a) : ')); #  starting point or lower limit of the area
    b = float(input('Please provide the upper limit (b) : ')); #  end point or upper limit of the area
    Simpson_Composite(fx,a,b,r)
    Trapezoid_Composite(fx,a,b,r)
    Calc = St.Numerical_Integration(fx,a,b) # if you are using Jupyter Note-Book you don't use St
    print(Calc)
    Calc.Graph()