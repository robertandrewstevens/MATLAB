# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 1
# MATLAB script refactored into Python (from R) - WIP
# comments are indicted by "#" instead of "%"
# need to use "print" to see results in Python (?)

from math import *
import cmath

# 1.1 A glorified calculator

print 2 + 1

print 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

print 2*3 - 4/5
print 2.0*3.0 - 4.0/5.0

print 2 * (3 - 4) / 5
print 2.0 * (3.0 - 4.0) / 5.0

print 2^16

# 1.2 Math functions

print sin(1)

print atan2(1, 1)

print e # exp(1) in MATLAB

print log(exp(3))

print sqrt(sin(0.5)^2 + cos(0.5)^2)

# 1.3 Documentation

#help(sin) # commented out (don't know how to do this in script mode)

#SIN(1) # comment out so script completes without (intentional) error

# 1.4 Variables

print pi

print pi * 3^2

print sin(pi/2)

print cmath.exp(i * pi)

print 3^2 + 4^2

print sqrt(3^2 + 4^2)

# 1.5 Assignment statements

x = 6 * 7
print x

fibanocci0 = 1
print fibannocci0

LENGTH = 10
print LENGTH

first_name = "allen"
print first_name

# 1.6 Why variables?

print e # "e = exp(1)" in MATLAB but just "e" in Python with math library

r = 3
print r

area = pi * r^2
print area

theta = 0 # define to avoid error message
sigma = 1 # define to avoid error message
zeta  = 0  # define to avoid error message

ans = ((x - theta) * sqrt(2.0 * pi) * sigma) ^ -1 *
	exp(-1.0/2.0 * (log(x - theta) - zeta)^2 / sigma^2)
print ans

shiftx = x - theta
demon = shiftx * sqrt(2.0 * pi) * sigma
temp = (log(shiftx) - zeta) / sigma
exponent = -1.0/2.0 * temp^2
ans = exp(exponent) / demon
print ans

# 1.7 Errors

area = pi * r^2 # corrected "area = pi r^2"
print area

print sin(1) * pi # corected "sin pi"

print abs(pi) # corrected "abs pi"

print 1 / 2 * sqrt(pi)

print 1 / (2 * sqrt(pi))

# 1.8 Floating-point arithmetic

print 1/3
print 1.0/3.0

print "%.14f" % 1/3 # instead of "format long" in MATLAB
print "%.14f" % 1.0/3.0 # instead of "format long" in MATLAB

print factorial(100)

speed_of_light = 3.0e8
print speed_of_light

print 1.7e+308 # "realmax" in MATLAB

print 2e-308 # "realmin" in MATLAB

print factorial(170)

print factorial(171)

print 1/0

print 0/0

# 1.9 Comments

speed_of_light = 3.0e8 # meters per second
print speed_of_light

x = 5 # assign the value 5 to x (avoid this type of comment)
print "x = ", x

p = 0    # postion from the origin in meters
print "p = ", p
v = 100  # velocity in meters / second
print "v = ", v
a = -9.8 # acceleration of gravity in meters / second^2
print "a = ", a
