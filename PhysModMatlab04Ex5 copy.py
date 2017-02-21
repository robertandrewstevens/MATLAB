# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.5 
# MATLAB script refactored into Python (via R)

# Write an expression that computes the sum of the squares of the
# elements of a vector.

import numpy as np

X = np.arange(1, 5 + 1, 1) # X <- 1:5 in R; X = 1:5 in MATLAB

total = 0
for i in range(0, len(X)):
    total = total + X[i]**2
print "total =", total