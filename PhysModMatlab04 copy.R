# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 4:  Vectors
# MATLAB script refactored into R

# 4.1 Checking preconditions

n <- -1

A1 <- 1
total <- 0
for(i in 1:n) {
  a <- A1 * 0.5^(i - 1)
  total <- total + a
}
total

1:-1

# 4.2 if

if(n < 0) {
  print(ans <- NA)
}

if(n < 0) {
  print(ans <- NA)
} else {
  A1 <- 1
  total <- 0
  for(i in 1:n) {
  a <- A1 * 0.5^(i - 1)
  total <- total + a
  }
  print(ans <- total)
}

# 4.3 Relational operators

x <- 5
x < 10

(flag <- x > 10)

#if x <- 5 # comment out intentional error so script runs

# 4.4 Logical operators

x <- 5
0 < x < 10 # right for the wrong reason

x <- 17
0 < x < 10 # just plain wrong

ans <- 0
if(0 < x) {
  if(x < 10) {
    ans <- 1
  }
}
ans

x <- 5
0 < x && x < 10

x <- 17
0 < x && x < 10

# 4.5 Vectors

(X <- 1:5)

# 4.6 Vector arithmetic

(Y <- X + 5)

(Z <- X + Y)

(W <- 1:3)

X + W # gives an error in MATLAB, but recycles values in R and gives a warning

# 4.7 Everything is a matrix

(scalar <- 5)

(vector <- 1:5)

(matrix <- matrix(1, nrow = 2, ncol = 3)) # ones(2, 3) in MATLAB

ls.str() # whos in MATLAB

(X <- 1:5)

(Y <- 1:5)

(Z <- X %*% Y) # gives an error in MATLAB

X * Y # X .* Y in MATAB

# 4.8 Indices

(Y <- 6:10)

Y[1]

Y[5]

i <- 1

Y[i + 1]

for(i in 1:5) {
  print(Y[i])
}

for(i in 1:length(Y)) {
  print(Y[i])
}

# 4.9 Indexing errors

#Y[0] # comment out intentional error so script runs

#Y[6] # comment out intentional error so script runs

#Y[1.5] # comment out intentional error so script runs

# 4.10 Vectors and sequences

n <- 10
F[1] <- 1
F[2] <- 1
for(i in 3:n) {
  F[i] <- F[i - 1] + F[i - 2]
}
print(F[n])

F[1] <- 1
F[2] <- 1
for(i in 1:(n - 2)) {
  F[i + 2] <- F[i + 1] + F[i]
}
print(F[n])

# 4.11 Plotting vectors

plot(F)

X <- 1:5
Y <- 6:10
plot(X, Y)

# 4.12 Reduce

total <- 0
for(i in 1:length(X)) {
  total <- total + X[i]
}
total

# 4.13 Apply

X <- 1:5 # redefine so example runs as intended (?)
for(i in 1:length(X)) {
  Y[i] <- X[i]^2
}
Y

# 4.14 Search

(X <- seq(from = 10, to = -10, by = -1)) # X = 10:-1:-10 in MATLAB

for(i in 1:length(X)) {
  if(X[i] == 0) {
    ans <- i
  }
}
ans

for(i in 1:length(X)) {
  if(X[i] == 0) {
    ans <- i
    break
  }
}
ans

X <- seq(from = 1, to = 2, len = 100) # X = linspace(1, 2) in MATLAB
for(i in 1:length(X)) {
  Y[i] <- sin(X[i])
}
plot(X, Y)

for(i in 1:length(Y)) {
  if(Y[i] == 0.9) {
    ans <- i
    break
  }
}
ans
Y[11:13] # R finds a match at i = 11 and Y = 0.891..., but MATLAB does not - why?

# 4.15 Spoiling the fun

(X <- 1:5) # redefine so example runs as intended (?)
(Y <- X^2) # Y = X .^ 2 in MATLAB

X <- seq(0, 2*pi, len = 100) # X = linspace(0, 2*pi) in MATLAB
Y <- sin(X)
plot(X, Y)
