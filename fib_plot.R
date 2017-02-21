# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.6
# MATLAB script refactored into R

# Loop through a range from 1 to 20, use fibonacci2 to compute 
# Fibonacci numbers, and plots Fi for each i with a series of red circles. 

plot(c(0, 20), c(0, 7000), xlab = "n", ylab = "Fibonacci Number", type = "n")

points(1, 1, col = "red", pch = 1); # n = 1, F1 = 1
points(2, 1, col = "red", pch = 1); # n = 2, F2 = 1
for(n in 3:20) { # replaced i with n in for looop and removed "n <- i"
  source("fibonacci2.R");
  points(i, ans, col = "red", pch = 1);
}