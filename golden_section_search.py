'''
The golden-section search is a technique for finding the extremum of a strictly unimodal function f(x).
description in the notes folder.
'''

import math
import numpy as np
import matplotlib.pyplot as plt


def golden_section_method_min(f, a, b, epsilon = 10**(-5), steps_limit = None):
    x1 = a + ((3-math.sqrt(5))/2.)*(b-a)  # first golden points
    x2 = a + ((math.sqrt(5)-1)/2.)*(b-a)  # fisrt golden points
    if steps_limit is None:
        while b-a>epsilon:
            if (f(x1) <= f(x2)):
                b = x2
                x2 = x1  # next golden points
                x1 = a+b-x2  # next golden points
            else:
                a = x1
                x1=x2  # next golden points
                x2 = a+b-x1  # next golden points
    else:
        s = 0
        while s<steps_limit:
            if (f(x1) <= f(x2)):
                b = x2
                x2 = x1  # next golden points
                x1 = a+b-x2  # next golden points
            else:
                a = x1
                x1=x2  # next golden points
                x2 = a+b-x1  # next golden points
            s+=1
    return x1 if f(x1) < f(x2)else x2

def golden_section_method_max(f, a, b, epsilon = 10**(-5), steps_limit = None):
    x1 = a + ((3-math.sqrt(5))/2.)*(b-a)  # first golden points
    x2 = a + ((math.sqrt(5)-1)/2.)*(b-a)  # fisrt golden points
    if steps_limit is None:
        while b-a>epsilon:
            if (f(x1) >= f(x2)):
                b = x2
                x2 = x1  # next golden points
                x1 = a+b-x2  # next golden points
            else:
                a = x1
                x1=x2  # next golden points
                x2 = a+b-x1  # next golden points
    else:
        s = 0
        while s<steps_limit:
            if (f(x1) >= f(x2)):
                b = x2
                x2 = x1  # next golden points
                x1 = a+b-x2  # next golden points
            else:
                a = x1
                x1=x2  # next golden points
                x2 = a+b-x1  # next golden points
            s+=1
    return x1 if f(x1) < f(x2)else x2


func_1 = lambda x: x**2 + 2*(x*math.log10(x/math.e)-2)
func_2 = lambda x: 1/x**2
func_3 = lambda x: x**2
func = func_2

a = -4.5
b = 4.0

x_val = []
y_val = []
for i in np.arange(a-4,b+4,0.1):
    try:
        print(f"x = {i}\t\tf(x) = {func(i)}")
        x_val.append(i)
        y_val.append(func(i))
    except ValueError as e:
        print(f"x = {i}\t\tf(x) = None")

plt.plot(x_val,y_val)

res = golden_section_method_min(func, a, b)
print(res)
print(func(res))
plt.show()