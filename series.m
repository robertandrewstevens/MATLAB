% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 3:  Loops
% Script for Exercise 3.4

% Compute the same sum by computing the elements recurrently. 

a = 1
r = 1/2
for i = 2:10
    a = a*r
end
