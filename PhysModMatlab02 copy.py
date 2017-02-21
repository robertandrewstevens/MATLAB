# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 2:  Scripts
# MATLAB script refactored into Python (via R) - WIP
# comments are indicted by "#" instead of "%"
# assignments use "<-" instead of "=" (although it's allowed, it is not recommneded)

from math import *
import myscript
#import fibanocci1

# 2.1 M-files

myscript

#my script # comment out so script completes without (intentional) error

# 2.2 Why scripts?

# No code in section 2.2

# 2.3 The workspace

x = 5
y = 7
z = 9
# "who" in MATLAB or objects() in R
# http://www.gossamer-threads.com/lists/python/python/565579
print "Your variables are:"
print [var for var in dir() if not (var.startswith('_') or var == 'var')]
print ""

# http://grokbase.com/t/python/tutor/07adweedqr/variables-in-workspace
del y # "clear y" in MATLAB or rm(y)  in R

print "Your variables are:"
print [var for var in dir() if not (var.startswith('_') or var == 'var')]
print ""
 
print ">> z = ", z # "disp(z)" in MATLAB
print ""

# 2.4 More errors

# "fibanocci1" from Exercise 2.1

#fibanocci1 # comment out so script completes without (intentional) error

n = 10
# http://stackoverflow.com/questions/5788891/execfile-with-argument-in-python-shell
import sys
sys.argv = ['fibanocci1.py','n']
execfile('fibanocci1.py')

# 2.5 Pre- and post-conditions

#help("fibanocci1.R") # comment out - 'help' is for commands or packages in R
#doc fibanocci1 # comment out - 'doc' is for internal fucntions in Python

# 2.6 Assignment and equality

y = 1
x = y + 1
print ">> x = ", x
print ""

#y + 1 = x % comment out so script completes without (intentional) error

y = 1
y = y + 1
print ">> y = ", y
print ""

# 2.7 Incremental development

# No code in section 2.7

# 2.8 Unit testing

print ">> asin(0) = ", asin(0.0)
print ""

print ">> asin(1) = ", asin(1.0)
print ""

print ">> asin(1) / pi = ", asin(1.0) / pi
print ""