# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Script for Exercise 4.8
# MATLAB script refactored into R

# Computes the first 50 elements of X given r and X1 = 0.5,
# where r is the parameter of the logistic map 
# and X1 is the initial population.

n <- 50
X <- as.numeric(rep(NA, n)) # initialize

X[1] = 0.5

for(j in 2:n) {
  X[j] <- r*X[j - 1]*(1 - X[j - 1])
}
