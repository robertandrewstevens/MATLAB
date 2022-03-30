# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# MATLAB script refactored into Python (via R)

from math import *
import numpy as np
import pylab as pl

# 4.1 Checking preconditions

n = -1

A1 = 1.0
total = 0.0
for i in range(1, n + 1):
    a = A1 * 0.5**(i - 1)
    total = total + a
print "ans =", total

print range(1, -1 -1, -1) # 1:-1 in R and MATLAB
print np.arange(1, -1 -1, -1) # 1:-1 in R and MATLAB

# 4.2 if

if n < 0:
    ans = np.nan
    print "ans =", ans

if n < 0:
    ans = np.nan
    print "ans =", ans
else:
    A1 = 1.0
    total = 0.0
    for i in range(1, n + 1):
        a = A1 * 0.5**(i - 1)
        total = total + a
    print "ans =", total

# 4.3 Relational operators

x = 5
print "x =", x
print "x < 10?", x < 10

flag = x > 10
print "flag =", flag

#if x = 5 # comment out intentional error so script runs

# 4.4 Logical operators

x = 5
print "x =", x
print "0 < x < 10?", 0 < x < 10 # right for the wrong reason

x = 17
print "x =", x
print "0 < x < 10?", 0 < x < 10 # just plain wrong

ans = 0
if 0 < x:
    if x < 10:
        ans = 1
print "ans =", ans

x = 5
print "x =", x
print "0 < x && x < 10?", 0 < x and x < 10

x = 17
print "x =", x
print "0 < x && x < 10?", 0 < x and x < 10

# 4.5 Vectors

X = np.arange(1, 5 + 1, 1) # (X <- 1:5) in R and X = 1:5 MATLAB
print "X =", X

# 4.6 Vector arithmetic

Y = X + 5
print "Y =", Y

Z = X + Y
print "Z =", Z

W = np.arange(1, 3 + 1, 1) # (W <- 1:3) in R and W = 1:3 MATLAB
print "W =", W

# X + W gives an error in MATLAB, but recycles values in R and gives a warning
#print "X + W =", X + W # commented out - in Python gives 
# "ValueError: operands could not be broadcast together with shapes (5) (3)"

# 4.7 Everything is a matrix

scalar = 5
print "scalar =", scalar

vector = np.arange(1, 5 + 1, 1) # (vector <- 1:5) in R
print "vector =", vector

# matrix = ones(2, 3) in MATLAB
# matrix <- matrix(1, nrow = 2, ncol = 3)) in R
matrix = np.ones((2, 3))
print "matrix =", matrix

# want equivalent of 'whos' in MATLAB and 'ls.str()' in R
# "who" in MATLAB or objects() in R
print "Your variables are:"
print [var for var in dir() if not (var.startswith('_') or var == 'var')]
print ""

X = np.arange(1, 5 + 1, 1) # (X <- 1:5) in R
print "X =", X

Y = np.arange(1, 5 + 1, 1) # (Y = 1:5) in R
print "Y =", Y

# (Z = X %*% Y) in R - gives an error in MATLAB
# X .* Y works in MATAB
Z = X*Y
print "Z =", Z

# 4.8 Indices

Y = np.arange(6, 10 + 1, 1) # (Y = 6:10) in R
print "Y =", Y

print "Y[0] =", Y[0]
print "Y[4] =", Y[4]

i = 1
print "i =", i
print "Y[i + 1] =", Y[i + 1]

for i in range(0, 5):
    print "i =", i,
    print "Y[i] =", Y[i]

for i in range(0, len(Y)):
    print "i =", i,
    print "Y[i] =", Y[i]

# 4.9 Indexing errors

#Y[0] # comment out intentional error so script runs

#Y[6] # comment out intentional error so script runs

#Y[1.5] # comment out intentional error so script runs

# 4.10 Vectors and sequences

n = 10

F = [] # initialize
F.append(1) # in F[1] = 1 in R; F(1) in MATLAB
F.append(1) # in F[2] = 1 in R; F(2) in MATLAB
for i in range(2, n):
    F.append(F[i - 1] + F[i - 2])
print "ans =", F[n - 1]

F = [] # initialize
F.append(1) # in F[1] = 1 in R; F(1) in MATLAB
F.append(1) # in F[2] = 1 in R; F(2) in MATLAB
for i in range(0, n - 1):
    F.append(F[i + 1] + F[i])
print "ans =", F[n - 1]

# 4.11 Plotting vectors

pl.plot(F, 'o')
pl.show()

X = np.arange(1, 5 + 1, 1) # 1:5 in MATLAB and R
Y = np.arange(6, 10 + 1, 1) # 6:10 in MATLAB and R
pl.plot(X, Y, 'o')
pl.show()

# 4.12 Reduce

total = 0
for i in range(0, len(X)):
    total = total + X[i]
print "ans =", total

# 4.13 Apply

# redefine X so example runs as intended (?)
X = np.arange(1, 5 + 1, 1) # 1:5 in MATLAB and R
Y = [] # initialize
for i in range(0, len(X)):
    Y.append(X[i]**2)
print "Y =", Y

# 4.14 Search

# X = 10:-1:-10 in MATLAB
# (X = seq(from = 10, to = -10, by = -1)) in R
X = np.arange(10, -10 - 1, -1)

for i in range(0, len(X)):
    if X[i] == 0:
        ans = i
print "ans =", ans

for i in range(0, len(X)):
    if X[i] == 0:
        ans = i
        break
print "ans =", ans

# X = linspace(1, 2) in MATLAB
# X = seq(from = 1, to = 2, len = 100) in R 
X = np.linspace(1, 2, num = 100) # similar to MATLAB
Y = [] # initialize
for i in range(0, len(X)):
    Y.append(sin(X[i]))
pl.plot(X, Y, 'o')
pl.show()

for i in range(0, len(Y)):
    if Y[i] == 0.9:
        ans = i
        break
print "ans =", ans

# 4.15 Spoiling the fun

# redefine so example runs as intended (?)
X = np.arange(1, 5 + 1, 1) # 1:5 in MATLAB and R
print "X =", X
Y = X**2 # (Y = X^2) in R and Y = X .^ 2 in MATLAB
print "Y =", Y

# X = linspace(0, 2*pi) in MATLAB
# X = seq(0, 2*pi, len = 100) in R
#X = np.linspace(0, 2*pi, num = 100) # simlar to MATLAB
X = np.arange(0, 2.0*pi, 2.0*pi/100.0)
# http://www.utdallas.edu/~jwz120030/Teaching/GradSciCtg/PythonDemos/Vectorization.py
Y = np.sin(X)
pl.plot(X, Y, 'o')
pl.show()
