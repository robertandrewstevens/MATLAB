# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.3
# MATLAB script refactored into Pyton (via R)

# Use a loop to compute elements of A directly:  A[i] = A1*r**(i - 1)

a1 = 1.0
r = 1.0/2.0
for i in range(2, 11):
    a = a1*r**(i - 1)
    print "a = ", a