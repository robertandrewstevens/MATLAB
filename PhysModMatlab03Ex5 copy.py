# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Exercise 3.5
# MATLAB script refactored into Pyton (via R)

# We have already seen the Fibonacci sequence, F, which is defined recurrently as
#    F[i] = F[i - 1] + F[i - 2]
# In order to get started, you have to specify the first two elements, but once 
# you have those, you can compute the rest. 
# The most common Fibonacci sequence starts with F1 = 1 and F2 = 1.

# Write a script called fibonacci2 that uses a for loop to compute the first 10 
# elements of this Fibonacci sequence. 
# As a postcondition, your script should assign the 10th element to ans.

# Now generalize your script so that it computes the nth element for any value of 
# n, with the precondition that you have to set n before you run the script. 
# To keep things simple for now, you can assume that n is greater than 2.

# Hint: you will have to use two variables to keep track of the previous two 
# elements of the sequence. 
# You might want to call them prev1 and prev2. 
# Initially, prev1 = F1 and prev2 = F2. 
# At the end of the loop, you will have to update prev1 and prev2; 
# think carefully about the order of the updates!

import sys

sys.argv = ['fibonacci2.py', 'n']

n = 10
execfile("fibonacci2.py")