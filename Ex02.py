# t(en)       | 0   |  10   |   20   |  30 |  40   |  50   |  60   | 70   |  80
# a(en m/s^2)| 30 | 31.63 | 33.44 | 35.47 | 37.75 | 40.33 | 43.28 | 46.70 |50.67

# we can't use the method of Trapezoid and Simpson Composite because they need a function which not in this case so we create two tables one for t(time) and the other for a (Acceleration)

import numpy as np

# Define acceleration array
a = np.array([30, 31.63, 33.44, 35.47, 37.75, 40.33, 43.28, 46.70, 50.67])


# f_a=30 ; f_b=50.67 # mean the f(a) = 30 , f(b) = 50.67

# Define endpoints and function values
f_a = 30
f_b = 50.67

# # we got n=8  there is eight point and a=0 b=80 so h=10 -- Method Trapezoid Composite

# n=8 ; h=10 ; a=0 ; b=80 
## 1- We Apply the Trapezoid Composite 

h = 10  # Interval width
n = len(a)  # Number of intervals
s1 = sum(2 * a[i] for i in range(1, n-1 ))
area_trapezoid = (h / 2) * (f_a + f_b + s1)
print('Trapezoid Integral =', area_trapezoid)







# we got n=8  there is eight point and a=0 b=80 so h=20 -- Method Simpson Composite
# n=8 ; h=20 ; a=0 ; b=80 
# 2- We Apply the Simpson's Composite 
h = 20  # Interval width
s1 = sum(2 * a[i] for i in range(2, n-1,2))
s2 = sum(4 * a[i] for i in range(1, n-1,2))
area_simpson = (h / 6) * (f_a + f_b + s1 + s2)
print('Simpson Integral =', area_simpson)
