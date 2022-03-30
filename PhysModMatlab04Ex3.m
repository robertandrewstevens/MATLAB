% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 4:  Vectors
% Exercise 4.3 

% Write a loop that computes a vector Y that contains the sines of
% the elements of X. 
% To test your loop, write a script that
% 1. Uses linspace (see the documentation) to assign to X a vector with 100
%    elements running from 0 to 2.
% 2. Uses your loop to store the sines in Y.
% 3. Plots the elements of Y as a function of the elements of X.

%echo on

X = linspace(0, 2);

for i = 1:length(X)
    Y(i) = sin(X(i));
end
plot(X, Y);

%echo off
