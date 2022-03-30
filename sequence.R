# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.3
# MATLAB script refactored into R

# Use a loop to compute elements of A directly:  A(i) = A1*r^(i − 1)

a1 <- 1
r <- 1/2
for(i in 2:10) {
    print(a <- a1*r^(i - 1))
}