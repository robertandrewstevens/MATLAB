% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 4:  Vectors
% Exercise 4.6

% The ratio of consecutive Fibonacci numbers, Fn+1/Fn, converges
% to a constant value as n increases. 
% Write a script that computes a vector with the first n elements of a 
% Fibonacci sequence (assuming that the variable n is defined), 
% and then computes a new vector that contains the ratios of consecutive
% Fibonacci numbers.
% Plot this vector to see if it seems to converge. 
% What value does it converge on?

echo on

n = 10;

F(1) = 1;
F(2) = 1;
for i = 1:n - 2
    F(i + 2) = F(i + 1) + F(i);
end

for i = 1:n - 1
    ratio(i + 1) = F(i + 1)/F(i);
end

plot(ratio);

echo off
