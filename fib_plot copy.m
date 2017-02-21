% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 3:  Loops
% Script for Exercise 3.6

% Loop through a range from 1 to 20, use fibonacci2 to compute 
% Fibonacci numbers, and plots Fi for each i with a series of red circles. 

hold on

plot(1, 1, "ro"); % i = 1
plot(2, 1, "ro"); % i = 2
for i = 3:20
    n = i
    fibonacci2;
    plot(i, ans, "ro");
end

hold off