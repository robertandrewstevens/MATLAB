# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 5:  Functions
# MATLAB script refactored into Python (via R)

def myfunc(x):
    # Compute the Manhattan distance from the origin to the
    # point on the unit circle with angle (x) in radians.
    s = sin(x)
    c = cos(x)
    res = abs(s) + abs(c)
    return res

# If change 'myfunc' to 'something_else'
def something_else(x):
    s = sin(x)
    c = cos(x)
    res = abs(s) + abs(c)
    return res

def mysum():
    res = 7
    return res

def hypotenuse(a, b):
    res = sqrt(a**2 + b**2)
    return res

# http://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def isPrime(num, div = 2):
    if(num == div):
        return True
    elif(num % div == 0):
        return False
    else:
        return isPrime(num, div + 1)

def isIntegral(x):
    if(round(x) == x):
        res = True
    else:
        res = False
    return res

def find_triples1():
    x = 5
    print "x = ", x

def find_triples2():
    for a in range(1, 3 + 1):
        print "a = ", a

def find_triples3():
    for a in range(1, 3 + 1):
        for b in range(1, 4 + 1):
            print "a = ", a, "b = ", b

def find_triples4():
    for a in range(1, 3 + 1):
        for b in range(1, 4 + 1):
            c = hypotenuse(a, b)
            print a, b, c # [a, b, c] in MATLAB

def find_triples5():
    for a in range(1, 3 + 1):
        for b in range(a, 4 + 1):
            c = hypotenuse(a, b)
            print a, b, c # [a, b, c] in MATLAB

def find_triples6():
    for a in range(1, 3 + 1):
        for b in range(a, 4 + 1):
            c = hypotenuse(a, b)
            flag = isIntegral(c)
            print c, flag # [c, flag] in MATLAB

def find_triples7():
    for a in range(1, 3 + 1):
        for b in range(a, 4 + 1):
            c = hypotenuse(a, b)
            flag = isIntegral(c)
            if(flag):
                print a, b, c # [a, b, c] in MATLAB

def find_triples8(n):
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = hypotenuse(a, b)
            flag = isIntegral(c)
            if(flag):
                print a, b, c # [a, b, c] in MATLAB

# https://answers.yahoo.com/question/index?qid=20120125211736AA32hEy
def GCD(a, b): 
    if(b == 0): 
        value = a 
        return value
    else: 
        value = GCD(b, a % b) # '%%' in R = mod(a, b) in MATLAB
        return value

def find_triples9(n):
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            if(GCD(a, b) > 1):
                continue # also 'continue' in MATLAB; 'next' in R
            c = hypotenuse(a, b)
            if(isIntegral(c)):
                print a, b, c # [a, b, c] in MATLAB