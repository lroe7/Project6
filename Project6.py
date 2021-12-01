# Lauren Roe
# CST-305
# This is my work

import numpy as np                  # imports the numpy package
import matplotlib.pyplot as plt     # imports the library for plotting the graphs
from scipy.integrate import odeint

# defines the function with the taylor polynomial equation from part 1a
def taylora(x):
    y = 1 - x - (1/3) * pow(x, 3) - (1/12) * pow(x, 4)          # the equation found using taylor polynomials in part 1a
    return y                                                    # returns the equation


# defines the function with the taylor polynomial equation from part 1b
def taylorb(x):
    y = 6 + (x-3) - (11/2)*(x-3)*(x-3)                          # the equation found using taylor polynomials in part 1b
    return y                                                    # returns the equation


# defines the equation from the power series equation found in part 2
def powerseries(x, a0, a1):
    # x0 is all the values multiplied by a0 in the equation found for part 2
    x0 = 1 - (1/8)*pow(x, 2) + (1/128)*pow(x, 4) - (13/15360)*pow(x, 6) + (403/3440640)*pow(x, 8) - (22971/1238630400)* pow(x, 10)
    # x0 is all the values multiplied by a0 in the equation found for part 2
    x1 = x - (1/24)*pow(x, 3) + (7/1920)*pow(x, 5) - (147/322560)*pow(x, 7) + (6321/92897280)*pow(x, 9)
    y = a0 * x0 + a1 * x1               # the equation found using power series in part 2
    return y                            # returns the equation


def model(f, p, k):
    dfdp = k / p
    return dfdp


x = np.linspace(2, 4, 100)              # the x values used for the taylor polynomial graphs
ya = []                                 # creates the array for the y values of part a
yb = []                                 # creates the array for the y values of part b

xpow = np.linspace(0, 10, 100)         # the x values used for the power series equation
ypow = []                               # creates the array for the y values of the power series equation

for i in range(0, 100):                 # runs through the loop 100 times
    ya.append(taylora(x[i]))            # adds the y values in the ya array for every x value

for i in range(0, 100):                 # runs through the loop 100 times
    yb.append(taylorb(x[i]))            # adds the y values in the yb array for every x value

for i in range(0, 100):                         # runs through the loop 100 times
    ypow.append(powerseries(xpow[i], 1, 1))     # adds the y values in the ypow array for every x value

p = np.linspace(1, 20)                          # values for p to plot
k = 100                                         # initial condition for the constant
f0 = 5                                          # initial condition for number of frames
framerate = odeint(model, f0, p, args=(k,))     # calculates the derivative of the function

plt.plot(x, ya)                         # plots the graph for part 1a
plt.title('part 1a taylor polynomial')  # titles the graph
plt.xlabel('x')                         # labels x-axis
plt.ylabel('y')                         # labels y-axis
plt.show()                              # shows the graph

plt.plot(x, yb)                         # plots the graph for part 1b
plt.title('part 1b taylor polynomial')  # titles the graph
plt.xlabel('x')                         # labels x-axis
plt.ylabel('y')                         # labels y-axis
plt.show()                              # shows the graph

plt.plot(xpow, ypow)                    # plots the graph for part 2
plt.title('part 2 power series')        # titles the graph
plt.xlabel('x')                         # labels x-axis
plt.ylabel('y')                         # labels y-axis
plt.show()                              # shows the graph

plt.plot(p, framerate)                  # plots the graphs for part 3
plt.title('part 3: ethernet fram rate') # titles the graph
plt.xlabel('x')                         # labels x-axis
plt.ylabel('y')                         # labels y-axis
plt.show()                              # shows the graph

