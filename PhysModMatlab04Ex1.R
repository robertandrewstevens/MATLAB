# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.1
# MATLAB script refactored into R

# Write a loop that computes the first n elements of the geometric
# sequence Ai+1 = Ai/2 with A1 = 1. 
# Notice that the math notation puts Ai+1 on the left side of the equality. 
# When you translate to MATLAB, you may want to shift the index.

n <- 10

A <- rep(0, n) # initialize
A[1] <- 1
for(i in 1:(n - 1)) {
  A[i + 1] <- A[i]/2
}
A
