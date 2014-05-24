# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.7 
# MATLAB script refactored into Python (via R)

# A certain famous system of differential equations can be approximated by 
# a system of difference equations that looks like this:
#    x(i + 1) = x(i) + s(y(i) - x(i)) dt           (4.1)
#    y(i + 1) = y(i) + [x(i)(r - z(i)) - y(i)] dt  (4.2)
#    z(i + 1) = z(i) + (x(i)y(i) - bz(i)) dt       (4.3)

# Write a script that computes the first 10 elements of the sequences X, Y
# and Z and stores them in vectors named X, Y and Z.
# Use the initial values X(1) = 1, Y(1) = 2 and Z(1) = 3, with values 
# s = 10, b = 8/3 and r = 28, and with time step dt = 0.01.

# Read the documentation for 'plot3' and 'comet3' and plot the results in 3
# dimensions.

# Once the code is working, use semicolons to suppress the output and then
# run the program with sequence length 100, 1000 and 10000.

# Run the program again with different starting conditions. 
# What effect does it have on the result?

# Run the program with different values for s, b and r and see if you can
# get a sense of how each variable affects the system.

import pylab as pl

#n = 10
#n = 100
#n = 1000
n = 10000

X = [] # initialize
Y = [] # initialize
Z = [] # initialize

X.append(1.0)
Y.append(2.0)
Z.append(3.0)

s = 10.0
b = 8.0/3.0
r = 28.0
dt = 0.01

for i in range(0, n):
    X.append(X[i] + s*(Y[i] - X[i])*dt)
    Y.append(Y[i] + (X[i]*(r - Z[i]) - Y[i])*dt)
    Z.append(Z[i] + (X[i]*Y[i] - b*Z[i])*dt)

#cloud(Z ~ X*Y) # plot3(X, Y, Z) in MATLAB

# http://stackoverflow.com/questions/9164950/python-matplotlib-plot3d-with-a-color-for-4d
x, y, z = X, Y, Z
fig = pl.figure()
from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
pl.show()

#plot3d(X, Y , Z) in R (allows rotation of axes)

# comet3(X, Y, Z) in MATLAB
# Can't find an analogous function in Python
