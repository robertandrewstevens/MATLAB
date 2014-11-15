# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.3 
# MATLAB script refactored into R

# Write a loop that computes a vector Y that contains the sines of
# the elements of X. 
# To test your loop, write a script that
# 1. Uses linspace (see the documentation) to assign to X a vector with 100
#    elements running from 0 to 2.
# 2. Uses your loop to store the sines in Y.
# 3. Plots the elements of Y as a function of the elements of X.

X <- seq(0, 2, len = 100) # X = linspace(0, 2) in MATLAB
Y <- rep(0, length(X)) # initialize

for(i in 1:length(X)) {
  Y[i] <- sin(X[i])
}
plot(X, Y)