# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 5:  Functions
# MATLAB script refactored into R

source("PhyModMatlab05Functions.R") # file for functions in Chapter 5

# 5.1 Name Collisions

A1 <- 1
total <- 0
for(i in 1:10) {
  a <- A1 * 0.5^(i - 1)
  total <- total + a
}
total

# 5.2 Functions

# add "myfunc" to "PhyModMatlab05Functions.R"

(myfunc(1))

(y = myfunc(1))

rm(list = ls()) # clear in MATLAB

source("PhyModMatlab05Functions.R") # need to "reinstall" functions

y = myfunc(1)

objects()

#s - comment out to avoid intentional error

s <- 1
c <- 1
y <- myfunc(1)
s
c

# 5.3 Documentation

# Add 3 lines of comments to beginning of 'myfunc'

# help myfunc # commented out - no similar functionality for user functions in R?

# 5.4 Function names

# If change 'myfunc' to 'something_else' and "reinstall" functions
source("PhyModMatlab05Functions.R")

(y <- myfunc(1))
(y = something_else(1))

#y = my func(1) #comment out intentional error

sum(1:3)

# Add function 'sum' to 'PhyModMatlab05Functions.R' and "reinstall" functions
source("PhyModMatlab05Functions.R")

(sum())

# 5.5 Multiple input variables

# Add function 'hypotenuse' to 'PhyModMatlab05Functions.R' and "reinstall" functions
source("PhyModMatlab05Functions.R")
(c <- hypotenuse(3, 4))

#c <- hypotenuse(3) #comment out intentional error

#c <- hypotenuse(3, 4, 5) #comment out intentional error

# 5.6 Logical functions

# Add function 'is.prime' to 'PhyModMatlab05Functions.R' and "reinstall" functions
source("PhyModMatlab05Functions.R")

is.prime(17)
is.prime(21)

(c <- hypotenuse(3, 4))
is.integer(c)

# Add function 'is.integral' to 'PhyModMatlab05Functions.R' and "reinstall" functions
# see help for 'is.integer' for fuction 'is.wholenumber' - same result?  TODO:  check
source("PhyModMatlab05Functions.R")
is.integral(c)

# 5.7 An incremental development example

# Add each version of 'find_tripples' function to 'PhyModMatlab05Functions.R' and "reinstall" functions
source("PhyModMatlab05Functions.R")

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
