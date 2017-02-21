# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.1
# MATLAB script refactored into Pyton (via R)

# Use a for loop to run car_update 52 times. 

import sys
import pylab as pl

a = 150 # initial number of cars in Albany
print "a = ", a 

b = 150 # initial number of cars in Boston
print "b = ", b

sys.argv = ['car_update.py', 'a', 'b']

for i in range(1, 53):
    execfile("car_update.py")
    pl.plot(i, a, 'ro')
    pl.plot(i, b, 'bD')
pl.show()