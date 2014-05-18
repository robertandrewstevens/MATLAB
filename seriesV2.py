# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# 3.8 Generalization
# MATLAB script refactored into Pyrhon (via R)

A1 = 1
total = 0
for i in range(1, n + 1): # instead of "for(i in 1:10)"
    a = A1 * 0.5**(i - 1)
    total = total + a
print "ans = %.14f" % total # instead of "format long" in MATLAB
