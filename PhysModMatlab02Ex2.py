# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 2:  Scripts
# Exercise 2.2
# MATLAB script refactored into Pyton (via R)

# Write a few lines of code that swap the values of x and y. 
# Put your code in a script called swap and test it.

import sys

x =  1 
y = 10 

sys.argv = ['swap.py', 'x', 'y']
execfile('swap.py')

print "x = ", x
print "y = ", y
