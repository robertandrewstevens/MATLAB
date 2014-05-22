% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 4:  Vectors
% Exercise 4.2 
# MATLAB script refactored into R

% Write a similar loop that multiplies all the elements of a vector
% together. 
% You might want to call the accumulator product, and you might want
% to think about the initial value you give it before the loop.

X <- 1:5

product = 1
for(i in 1:length(X)) {
  product <- product * X[i]
}
product
