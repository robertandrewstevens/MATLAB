# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.4
# MATLAB script refactored into R

# Compute the same sum by computing the elements recurrently. 

a <- 1
r <- 1/2
for(i in 2:10) {
  print(a <- a*r)
}
