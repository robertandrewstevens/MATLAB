# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.6
# MATLAB script refactored into Python (via R)

# The ratio of consecutive Fibonacci numbers, Fn+1/Fn, converges
# to a constant value as n increases. 
# Write a script that computes a vector with the first n elements of a 
# Fibonacci sequence (assuming that the variable n is defined), 
# and then computes a new vector that contains the ratios of consecutive
# Fibonacci numbers.
# Plot this vector to see if it seems to converge. 
# What value does it converge on?

import pylab as pl

n = 10
F = [] # initialize

F.append(1.0) # F[1] <- 1 in R
F.append(1.0) # F[2] <- 1 in R
for i in range(0, n - 2):
    F.append(F[i + 1] + F[i])
print "F =", F

ratio = [] # initialize
for i in range(0, n - 1):
    ratio.append(F[i + 1]/F[i])
print "Fi+1/Fi =", ratio

pl.plot(ratio, 'o')
pl.show()
