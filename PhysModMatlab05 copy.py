# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 5:  Functions
# MATLAB script refactored into Python (via R)

from math import *

execfile("PhysModMatlab05Functions.py") # file for functions in Chapter 5

# 5.1 Name Collisions

A1 = 1.0
total = 0.0
for i in range(1, 10 + 1):
  a = A1 * 0.5**(i - 1)
  total = total + a
print "total =", total

# 5.2 Functions

# add "myfunc" to "PhysModMatlab05Functions.py"

print "myfunc(1) =", myfunc(1)

y = myfunc(1)
print "y = ", y

# http://grokbase.com/t/python/tutor/07adweedqr/variables-in-workspace
del y # "clear y" in MATLAB or rm(y)  in R

# http://www.gossamer-threads.com/lists/python/python/565579
print "Your variables are:"
print [var for var in dir() if not (var.startswith('_') or var == 'var')]
print ""

y = myfunc(1)

print "Your variables are:"
print [var for var in dir() if not (var.startswith('_') or var == 'var')]
print ""

#s - comment out to avoid intentional error

s = 1
c = 1
y = myfunc(1)
print "s =", s
print "c =", c

# 5.3 Documentation

# Add 3 lines of comments to beginning of 'myfunc'

# help myfunc # commented out - no similar functionality for user functions in R?

# 5.4 Function names

# If change 'myfunc' to 'something_else'

y <- myfunc(1)
print "y =", y
y = something_else(1)
print "y =", y

#y = my func(1) #comment out intentional error

print "sum(1:3) =", sum([1, 2, 3])

# Add function 'mysum' to 'PhysModMatlab05Functions.py'
# conflict with 'sum' function in Python

print "mysum() =", mysum()

# 5.5 Multiple input variables

# Add function 'hypotenuse' to 'PhysModMatlab05Functions.py'
c <- hypotenuse(3, 4)
print "c =", c

#c <- hypotenuse(3) #comment out intentional error

#c <- hypotenuse(3, 4, 5) #comment out intentional error

# 5.6 Logical functions

# Add function 'isPrime' to 'PhysModMatlab05Functions.py'

print "Is 17 a prime number?", isPrime(17)
print "Is 21 a prime number?", isPrime(21)

c = hypotenuse(3, 4)
# http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
print "Is the hypotenuse(3, 4) an integer?", isinstance(c, int)

# Add function 'is.integral' to 'PhysModMatlab05Functions.py'
# see help for 'is.integer' for fuction 'is.wholenumber' - same result?  TODO:  check
print "Is the hypotenuse(3, 4) a whole number?", isIntegral(c)

# 5.7 An incremental development example

# Add each version of 'find_tripples' function to 'PhysModMatlab05Functions.py'

find_triples1()

find_triples2()

# 5.8 Nested loops

find_triples3()

find_triples4()

find_triples5()

# 5.9 Conditions and flags

find_triples6()

find_triples7()

# 5.10 Encapsulation and generalization

find_triples7

find_triples8(15)

# 5.11 A misstep

# If change 'hypotenuse.m' to
# hypotenuse <- function(a, b, d) {
#    res <- (a^d + b^d)^(1/d)
# }

#find_triples8(20) #comment out intentional error

# 5.12 continue

find_triples9(40)

# 5.13 Mechanism and leap of faith - no code in this section