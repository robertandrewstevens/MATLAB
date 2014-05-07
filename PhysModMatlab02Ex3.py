# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 2:  Scripts
# Exercise 2.3
# MATLAB script refactored into R

# Imagine that you are the owner of a car rental company with two locations,
# Albany and Boston. 
# Some of your customers do one-way rentals, picking up a car in Albany
# and returning it in Boston, or the other way around.
# Over time, you have observed that each week 5% of the cars in Albany are
# dropped off in Boston, and 3% of the cars in Boston get dropped off in 
# Albany.

# At the beginning of the year, there are 150 cars at each location.
# Write a script called car update that updates the number of cars in each 
# location from one week to the next. 
# The precondition is that the variables a and b contain the number of cars
# in each location at the beginning of the week.
# The postcondition is that a and b have been modified to reflect the 
# number of cars that moved.

# To test your program, initialize a and b at the prompt and then execute 
# the script.
# The script should display the updated values of a and b, but not any
# intermediate variables.

# Note: cars are countable things, so a and b should always be integer values.
# You might want to use the round function to compute the number of cars
# that move during each week.

# If you execute your script repeatedly, you can simulate the passage of 
# time from week to week.
# What do you think will happen to the number of cars?
# Will all the cars end up in one place? 
# Will the number of cars reach an equilibrium, or will it oscillate from
# week to week?

# In the next chapter we will see how to execute your script automatically, 
# and how to plot the values of a and b versus time.

import sys

a = 150 # initial number of cars in Albany
b = 150 # initial number of cars in Boston

sys.argv = ['carUpdate.py', 'a', 'b']
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
execfile('carUpdate.py')
