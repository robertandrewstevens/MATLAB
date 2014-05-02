# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 1:  Variables and values
# MATLAB script refactored into Python (from R) 
# comments are indicted by "#" instead of "%"
# need to use "print" to see results in Python
# Power operand "^" in MATLAB and R is "**" in Python

from math import *
import cmath


print ""
print ">> 1.1 A glorified calculator"
print ""

print ">> 2 + 1 = ", 2 + 1
print ""

print "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = ", 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
print ""

print ">> 2*3 - 4/5 = ", 2*3 - 4/5
print ">> 2.0*3.0 - 4.0/5.0 = ", 2.0*3.0 - 4.0/5.0
print ""

print ">> 2 * (3 - 4) / 5 = ", 2 * (3 - 4) / 5
print ">> 2.0 * (3.0 - 4.0) / 5.0 = ", 2.0 * (3.0 - 4.0) / 5.0
print ""

print ">> 2^16 = ", 2**16
print ""

print "1.2 Math functions"
print ""

print ">> sin(1) = ", sin(1)
print ""

print ">> atan2(1, 1) = ", atan2(1, 1)
print ""

print ">> exp(1) = ", e
print ""

print ">> log(exp(3)) = ", log(exp(3))
print ""

print ">> sqrt(sin(0.5)^2 + cos(0.5)^2) = ", sqrt(sin(0.5)**2 + cos(0.5)**2)
print ""

print "1.3 Documentation"
print ""

#help(sin) # commented out (don't know how to do this in script mode)

#SIN(1) # comment out so script completes without (intentional) error

print "1.4 Variables"
print ""

print ">> pi = ", pi
print ""

print ">> pi * 3^2 = ", pi * 3**2
print ""

print ">> sin(pi/2) = ", sin(pi/2)
print ""

print ">> exp(i * pi) = ", cmath.exp(cmath.sqrt(-1) * pi)
print ""

print ">> 3^2 + 4^2 = ", 3**2 + 4**2
print ""

print ">> sqrt(3^2 + 4^2) = ", sqrt(3**2 + 4**2)
print ""

print "1.5 Assignment statements"
print ""

x = 6 * 7
print ">> x = 6 * 7 = ", x
print ""

fibanocci0 = 1
print ">> fibanocci0 = ", fibanocci0
print ""

LENGTH = 10
print ">> LENGTH = ", LENGTH
print ""

first_name = "allen"
print ">> first_name = ", first_name
print ""

print "1.6 Why variables?"
print ""

print ">> e = exp(1) = ", e
print ""

r = 3
print ">> r = ", r
print ""

area = pi * r**2
print ">> area = ", area
print ""

theta = 0 # define to avoid error message
sigma = 1 # define to avoid error message
zeta  = 0  # define to avoid error message

ans = ((x-theta)*sqrt(2.0*pi)*sigma)**-1*exp(-1.0/2.0*(log(x-theta)-zeta)**2/sigma**2)
print ">> ans = ", ans
print ""

shiftx = x - theta
demon = shiftx * sqrt(2.0 * pi) * sigma
temp = (log(shiftx) - zeta) / sigma
exponent = -1.0/2.0 * temp**2
ans = exp(exponent) / demon
print ">> ans = ", ans
print ""

print "1.7 Errors"
print ""

area = pi * r**2 # corrected "area = pi r**2"
print ">> area = ", area
print ""

print ">> sin(1) * pi = ", sin(1) * pi # corected "sin pi"
print ""

print ">> abs(pi) = ", abs(pi) # corrected "abs pi"
print ""

print ">> 1 / 2 * sqrt(pi) = ", 1 / 2 * sqrt(pi)
print ""

print ">> 1 / (2 * sqrt(pi)) = ", 1 / (2 * sqrt(pi))
print ""

print "1.8 Floating-point arithmetic"
print ""

print ">> 1/3 = ", 1/3
print ">> 1.0/3.0 = ", 1.0/3.0
print ""

OneThird = 1.0/3.0
print ">> 1.0/3.0 = %.14f" % OneThird # instead of "format long" in MATLAB
print ""

print ">> 100! = ", factorial(100)
print ""

speed_of_light = 3.0e8
print ">> speed_of_light = ", speed_of_light
print ""

print ">> realmax = " , 1.7e+308 # value from R - higher in Python?
print ""

print ">> realmin = ", 2e-308 # value from R - smaller in Python?
print ""

print ">> 170! = ", factorial(170)
print ""

print ">> 171! = ", factorial(171) # not the max value like MATLAB and R
print ""

#print 1.0/0.0 # ZeroDivisionError: float division by zero - "Inf" in Python?

#print 0.0/0.0 # ZeroDivisionError: float division by zero - "NaN" in Python?

print "1.9 Comments"
print ""

speed_of_light = 3.0e8 # meters per second
print ">> speed_of_light = ", speed_of_light
print ""

x = 5 # assign the value 5 to x (avoid this type of comment)
print ">> x = ", x
print ""

p = 0    # postion from the origin in meters
print ">> p = ", p
v = 100  # velocity in meters / second
print ">> v = ", v
a = -9.8 # acceleration of gravity in meters / second^2
print ">> a = ", a
print ""
