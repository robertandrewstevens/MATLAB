# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# MATLAB script refactored into R

# 3.1 Updating variables - No code in section

# 3.2 Kinds of error - No code in section

# 3.3 Absolute and relative error - No code in section

# 3.4 for loops

a <- 150;
b <- 150;
for(i in 1:52) {
  source("carUpdate.R") # renamed from "car_update"
}

1:5

for(i in 1:5) {
  print(i)
}

# 3.5 plotting

par(pty = "s")

plot(1, 2, xlim = c(1, 2), ylim = c(1, 2), xlab = "", ylab = "")

plot(1, 2, pch = 16, xlim = c(1, 2), ylim = c(1, 2), xlab = "", ylab = "")

plot(1, 2, pch = 1, col = "red", xlim = c(1, 2), ylim = c(1, 2), xlab = "", ylab = "")

plot(1, 1, pch = 1, xlim = c(1, 2), ylim = c(1, 2), xlab = "", ylab = "")
points(2, 2, pch = 16, col = "red")

par(pty = "m")

# 3.6 Sequences

a <- 1
for(i in 2:10) {
  print(a <- a/2)
}

# 3.7 Series

A1 <- 1;
total <- 0;
for(i in 1:10) {
  a <- A1 * 0.5^(i - 1);
  total <- total + a;
}
(ans <- total)

# 3.8 Generalization

# modify script "series.R" from Exercise 3.4

options(digits = 14) # instead of "format long" in MATLAB

n <- 10; source("seriesV2.R")
n <- 20; source("seriesV2.R")
n <- 30; source("seriesV2.R")
n <- 40; source("seriesV2.R")
