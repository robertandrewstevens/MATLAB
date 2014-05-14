# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# Script for Exercise 3.1
# MATLAB script refactored into R

# Use a for loop to run car_update 52 times. 

print(a <- 150) # initial number of cars in Albany
print(b <- 150) # initial number of cars in Boston

for(i in 1:52) {
  source("car_update.R")
}
