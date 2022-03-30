% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 4:  Vectors
% Script for Exercise 4.8

% Computes the first 50 elements of X given r and X1 = 0.5,
% where r is the parameter of the logistic map 
% and X1 is the initial population.

n = 50;
X(1) = 0.5;

for i = 1:n - 1
    X(i + 1) = r*X(i)*(1 - X(i));
end
