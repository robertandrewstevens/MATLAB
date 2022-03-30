# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Script for Exercise 4.8
# MATLAB script refactored into Python (via R)

# Computes the first 50 elements of X given r and X1 = 0.5,
# where r is the parameter of the logistic map 
# and X1 is the initial population.

n = 50
X = [] # initialize

X.append(0.5)

for j in range(1, n):
    X.append(r*X[j - 1]*(1 - X[j - 1]))
