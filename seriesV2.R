# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 3:  Loops
# 3.8 Generalization
# MATLAB script refactored into R

A1 <- 1;
total <- 0;
for(i in 1:n) { # instead of "for(i in 1:10)"
  a <- A1 * 0.5^(i - 1);
  total <- total + a;
}
print(ans <- total)
