# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# Exercise 4.4 
# MATLAB script refactored into R

# Write a loop that finds the index of the first negative number in
# a vector and stores it in ans. 
# If there are no negative numbers, it should set ans to -1 (which is 
# not a legal index, so it is a good way to indicate the special case).

X <- seq(0, 2*pi, len = 100)
Y <- rep(NA, length(X))
for(i in 1:length(X)) {
  Y[i] <- sin(X[i])
}
plot(X, Y)

ans <- -1
for(i in 1:length(Y)) {
  if(Y[i] < 0) {
    ans <- i
    break
  }
}
ans

X <- seq(0, pi, len = 100) # check when no negative numbers
Y <- rep(NA, length(X))
for(i in 1:length(X)) {
  Y[i] <- sin(X[i])
}
plot(X, Y)

ans <- -1
for(i in 1:length(Y)) {
  if(Y[i] < 0) {
    ans <- i
    break
  }
}
ans