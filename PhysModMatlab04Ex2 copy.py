# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.2 
# MATLAB script refactored into Python (via R)

# Write a similar loop that multiplies all the elements of a vector
# together. 
# You might want to call the accumulator product, and you might want
# to think about the initial value you give it before the loop.

import numpy as np

X = np.arange(1, 5 + 1, 1) # X <- 1:5 in R; X = 1:5 in MATLAB

product = 1
for i in range(0, len(X)):
    product = product * X[i]
print "product =", product