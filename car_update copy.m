% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 2:  Scripts
% Script for Exercise 2.3

% Updates the number of cars in each location from one week to the next. 
% Precondition:  the variables a and b contain the number of cars in each 
% location at the beginning of the week.
% Postcondition:  a and b have been modified to reflect the number of cars
% that moved.

aRate = 0.05; % Rate of cars in Albany dropped off in Boston
bRate = 0.03; % Rate of cars in Boston dropped off in Albany

atob = round(aRate*a - bRate*b); % Number of cars moved from Albany to Boston

a = a - atob % Number of cars remaining in Albany
b = b + atob % Number of cars remaining in Boston