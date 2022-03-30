# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.4
# MATLAB script refactored into Pyton (via R)

# Compute the same sum by computing the elements recurrently. 

a = 1.0
r = 1.0/2.0
for i in range(2, 11):
    a = a*r
    print "a = ", a
