# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 1
# Exercise 1.1
# Write a MATLAB expression that evaluates the following math expression.
# You can assume that the variables mu, sigma and x already exist.

# MATLAB script refactored into Python (from R)
# scipy.stats.norm.pdf help from
# http://stackoverflow.com/questions/8669235/alternative-for-scipy-stats-norm-pdf

from math import *
import scipy.stats

mu = 0.8 # mean
sigma = 0.3 # standard deviation
x = 1 # value of random variable from a Normal distribution with mu and sigma

insideExp = (x - mu) / (sigma * sqrt(2.0))
exponent = -insideExp**2
demon = sigma * sqrt(2.0 * pi)
ans = exp(exponent) / demon

print ""
print ">> ans = ", ans
print ""

print ">> check = ", scipy.stats.norm.pdf(x, mu, sigma)
print ""
