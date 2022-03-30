% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 3:  Loops
% Exercise 3.5

% Computes the nth Fibonacci number.
% Precondition: you must assign a value to n before running this script.
%       Assume that n is greater than 2.
% Postcondition: assign the 10th element to ans.

prev1 = 1
prev2 = 1

total = 0;
for i = 3:n
    total =  prev1 + prev2
    prev2 = prev1;
    prev1 = total;
end
ans = total
