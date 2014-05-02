% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 1:  Variables and values
% Exercise 1.1
% Write a MATLAB expression that evaluates the following math expression.
% You can assume that the variables mu, sigma and x already exist.

echo on

mu = 0.8 % mean
sigma = 0.3 % standard deviation
x = 1 % value of random variable from a Normal distribution with mu and sigma

insideExp = (x - mu) / (sigma * sqrt(2))
exponent = -insideExp^2
demon = sigma * sqrt(2 * pi)
ans = exp(exponent) / demon

% check
normpdf(x, mu, sigma)
