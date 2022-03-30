# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.4 
# MATLAB script refactored into Python (via R)

# Write a loop that finds the index of the first negative number in
# a vector and stores it in ans. 
# If there are no negative numbers, it should set ans to -1 (which is 
# not a legal index, so it is a good way to indicate the special case).

from math import *
import numpy as np
import pylab as pl

# X <- seq(0, 2*pi, len = 100) in R
X = np.linspace(0.0, 2.0*pi, num = 100) # simlar to MATLAB
Y = [] # initialize

for i in range(0, len(X)):
    Y.append(sin(X[i]))
pl.plot(X, Y, 'o')
pl.show()

ans = -1
for i in range(0, len(Y)):
    if Y[i] < 0:
        ans = i
        break
print "ans =", ans
 
X = np.linspace(0.0, pi, num = 100) # check when no negative numbers
Y = [] # initialize

for i in range(0, len(X)):
    Y.append(sin(X[i]))
pl.plot(X, Y, 'o')
pl.show()

ans = -1
for i in range(0, len(Y)):
    if Y[i] < 0:
        ans = i
        break
print "ans =", ans
