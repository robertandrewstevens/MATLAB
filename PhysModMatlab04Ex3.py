# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.3 
# MATLAB script refactored into Python (via R)

# Write a loop that computes a vector Y that contains the sines of
# the elements of X. 
# To test your loop, write a script that
# 1. Uses linspace (see the documentation) to assign to X a vector with 100
#    elements running from 0 to 2.
# 2. Uses your loop to store the sines in Y.
# 3. Plots the elements of Y as a function of the elements of X.

from math import *
import numpy as np
import pylab as pl

# X = linspace(0, 2) in MATLAB
# X <- seq(0, 2, len = 100) in R
X = np.linspace(0, 2, num = 100) # simlar to MATLAB
Y = [] # initialize

for i in range(0, len(X)):
    Y.append(sin(X[i]))
pl.plot(X, Y, 'o')
pl.show()
