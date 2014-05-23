# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.1
# MATLAB script refactored into Pyton (via R)

# Write a loop that computes the first n elements of the geometric
# sequence Ai+1 = Ai/2 with A1 = 1. 
# Notice that the math notation puts Ai+1 on the left side of the equality. 
# When you translate to MATLAB, you may want to shift the index.

n = 10

A = [] # initialize
A.append(1.0)
for i in range(0, n - 1):
    A.append(A[i]/2.0)
print "A =", A
