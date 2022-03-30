# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# MATLAB script refactored into Python (via R)

import sys
import numpy as np
import pylab as pl

# 3.1 Updating variables - No code in section

# 3.2 Kinds of error - No code in section

# 3.3 Absolute and relative error - No code in section

# 3.4 for loops

sys.argv = ['carUpdate.py', 'a', 'b']

a = 150
b = 150
for i in range(1, 53):
    execfile('carUpdate.py') # renamed from "car_update.py"

print range(1, 6) # 1:5 in MATLAB and R

for i in range(1, 6):
    print "i = ", i
    
# 3.5 plotting

pl.plot(1, 2, 'bo')
pl.show()

pl.plot(1, 2, 'o')
pl.show()

pl.plot(1, 2, 'ro')
pl.show()

pl.plot(1, 1, 'o')
pl.plot(2, 2, 'o')
pl.show()

# 3.6 Sequences

a = 1.0
for i in range(2, 11):
    a = a/2.0
    print "a = ", a

# 3.7 Series

A1 = 1
total = 0
for i in range(1, 11):
    a = A1 * 0.5**(i - 1)
    total = total + a
print "ans = ", total

# 3.8 Generalization

# modify script "series.py" from Exercise 3.4

sys.argv = ['seriesV2.py', 'n']

n = 10
print "n = ", n
execfile("seriesV2.py")

n = 20
print "n = ", n
execfile("seriesV2.py")

n = 30
print "n = ", n
execfile("seriesV2.py")

n =  40
print "n = ", n
execfile("seriesV2.py")