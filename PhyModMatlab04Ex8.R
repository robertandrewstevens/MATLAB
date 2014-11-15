# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.8
# MATLAB script refactored into R

# The logistic map is often cited as an example of how complex, chaotic 
# behaviour can arise from simple non-linear dynamical equations [some of
# this description is adapted from the Wikipedia page on the logistic map].
# It was popularized in a seminal 1976 paper by the biologist Robert May.

# It has been used to model the biomass of a species in the presence of 
# limiting factors such as food supply and disease.
# In this case, there are two processes at work:
# (1) A reproductive process increases the biomass of the species in 
#     proportion to the current population.
# (2) A starvation process causes the biomass to decrease at a rate 
#     proportional to the carrying capacity of the environment less the 
#     current population.

# Mathematically this can be written as
#   X(i + 1) = rX(i)(1 - X(i))
# where X(i) is a number between zero and one that represents the biomass
# at year i, and r is a positive number that represents a combined rate 
# for reproduction and starvation.

# Write a script named 'logmap' that computes the first 50 elements of X
# with r = 3.9 and X1 = 0.5, where r is the parameter of the logistic map 
# and X1 is the initial population.

# Plot the results for a range of values of r from 2.4 to 4.0. 
# How does the behavior of the system change as you vary r.

# One way to characterize the effect of r is to make a plot with r on the
# x-axis and biomass on the y axis, and to show, for each value of r, the
# values of biomass that occur in steady state. 
# See if you can figure out how to generate this plot.

r <- 3.9
source("logmap.R")
plot(X)

rVec <- seq(2.4, 4.0, len = 100)
yVec <- as.numeric(rep(0, length(rVec)))

for(i in 1:length(rVec)) {
  r <- rVec[i]
  source("logmap.R")
  yVec[i] <- X[n]
}
plot(rVec, yVec, pch = 16, col = "red")
