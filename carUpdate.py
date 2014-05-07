# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 2:  Scripts
# Script for Exercise 2.3
# MATLAB script refactored into Python (via R)

# Updates the number of cars in each location from one week to the next. 
# Precondition:  the variables a and b contain the number of cars in each 
# location at the beginning of the week.
# Postcondition:  a and b have been modified to reflect the number of cars
# that moved.

aRate = 0.05; # Rate of cars in Albany dropped off in Boston
bRate = 0.03; # Rate of cars in Boston dropped off in Albany

aMove = round(aRate * a); # Number of cars moved from Albany to Boston
bMove = round(bRate * b); # Number of cars moved from Boston to Albany

a = a - aMove + bMove # Number of cars remaining in Albany
b = b - bMove + aMove # Number of cars remaining in Boston
print "a = ", a
print "b = ", b
