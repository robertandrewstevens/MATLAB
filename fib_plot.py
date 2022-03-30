# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.6
# MATLAB script refactored into Pyton (via R)

# Loop through a range from 1 to 20, use fibonacci2 to compute 
# Fibonacci numbers, and plots Fi for each i with a series of red circles. 

import sys
import pylab as pl

sys.argv = ['fibonacci2.py', 'n']

pl.plot(1, 1, 'ro') # n = 1, F1 = 1
pl.plot(2, 1, 'ro') # n = 2, F2 = 1
for n in range(3, 21):
  execfile("fibonacci2.py")
  pl.plot(i, total, 'ro')
pl.show()
