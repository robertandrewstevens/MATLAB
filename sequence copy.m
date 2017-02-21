% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 3:  Loops
% Script for Exercise 3.3

% Use a loop to compute elements of A directly:  A(i) = A1*r^(i − 1)

a1 = 1
r = 1/2
for i = 2:10
    a = a1*r^(i - 1)
end
