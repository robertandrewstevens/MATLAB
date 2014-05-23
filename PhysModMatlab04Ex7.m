% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 4:  Vectors
% Exercise 4.7 

% A certain famous system of differential equations can be approximated by 
% a system of difference equations that looks like this:
%    x(i + 1) = x(i) + s(y(i) - x(i)) dt           (4.1)
%    y(i + 1) = y(i) + [x(i)(r - z(i)) - y(i)] dt  (4.2)
%    z(i + 1) = z(i) + (x(i)y(i) - bz(i)) dt       (4.3)

% Write a script that computes the first 10 elements of the sequences X, Y
% and Z and stores them in vectors named X, Y and Z.
% Use the initial values X(1) = 1, Y(1) = 2 and Z(1) = 3, with values 
% s = 10, b = 8/3 and r = 28, and with time step dt = 0.01.

% Read the documentation for 'plot3' and 'comet3' and plot the results in 3
% dimensions.

% Once the code is working, use semicolons to suppress the output and then
% run the program with sequence length 100, 1000 and 10000.

% Run the program again with different starting conditions. 
% What effect does it have on the result?

% Run the program with different values for s, b and r and see if you can
% get a sense of how each variable affects the system.

echo on

%n = 10;
%n = 100;
%n = 1000;
n = 10000;

X(1) = 1;
Y(1) = 2;
Z(1) = 3;

s = 15; %5; %10;
b = 16/7; %8/3;
r = 7; %14; %28;
dt = 0.01;

for i = 1:n - 1
    X(i + 1) = X(i) + s*(Y(i) - X(i))*dt;
    Y(i + 1) = Y(i) + (X(i)*(r - Z(i)) - Y(i))*dt;
    Z(i + 1) = Z(i) + (X(i)*Y(i) - b*Z(i))*dt;
end

figure(1)
plot3(X, Y, Z)
hold on 

figure(2)
comet3(X, Y, Z)
hold off

echo off
