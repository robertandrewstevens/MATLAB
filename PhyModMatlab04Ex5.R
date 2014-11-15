# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.5 
# MATLAB script refactored into R

# Write an expression that computes the sum of the squares of the
# elements of a vector.

X <- 1:5

total <- 0
for(i in 1:length(X)) {
  total <- total + X[i]^2
}
total