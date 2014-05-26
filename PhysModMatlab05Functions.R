# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 5:  Functions
# MATLAB functions refactored into R

myfunc <- function (x) {
  # Compute the Manhattan distance from the origin to the
  # point on the unit circle with angle (x) in radians.
  s <- sin(x)
  c <- cos(x)
  res <- abs(s) + abs(c)
}

# If change 'myfunc' to 'something_else'
something_else <- function(x) {
  s <- sin(x)
  c <- cos(x)
  res <- abs(s) + abs(c);
}

sum <- function() {
  res <- 7
}

hypotenuse <- function(a, b) {
  res <- sqrt(a^2 + b^2)
}

# http://stackoverflow.com/questions/19767408/r-prime-number-function
is.prime <- function(n) n == 2L || all(n %% 2L:ceiling(sqrt(n)) != 0)

is.integral <- function(x) {
  if(round(x) == x) {
    res <- 1 # TRUE
  } else {
    res <- 0 # FASLSE
  }
  res
}

find_triples1 <- function () {
  x <- 5
  cat("x = ", x, "\n")
}

find_triples2 <- function() { 
  for(a in 1:3) {
    cat("a = ", a, "\n")
  }
}

find_triples3 <- function() {
  for(a in 1:3) {
    for(b in 1:4) {
      cat("a = ", a, "b = ", b, "\n")
    }
  }
}

find_triples4 <- function() {
  for(a in 1:3) {
    for(b in 1:4) {
      c <- hypotenuse(a, b)
      print(cbind(a, b, c)) # [a, b, c] in MATLAB
    }
  }
}

find_triples5 <- function() {
  for(a in 1:3) {
    for(b in a:4) {
      c <- hypotenuse(a, b)
      print(cbind(a, b, c)) # [a, b, c] in MATLAB
    }
  }
}

find_triples6 <- function() {
  for(a in 1:3) {
    for(b in a:4) {
      c <- hypotenuse(a, b)
      flag <- is.integral(c)
      print(cbind(c, flag)) # [c, flag] in MATLAB
    }
  }
}

find_triples7 <- function() {
  for(a in 1:3) {
    for(b in a:4) {
      c <- hypotenuse(a, b)
      flag <- is.integral(c)
      if(flag) {
        print(cbind(a, b, c)) # [a, b, c] in MATLAB
      }
    }
  }
}

find_triples8 <- function(n) {
  for(a in 1:n) {
    for(b in a:n) {
      c <- hypotenuse(a, b)
      flag <- is.integral(c)
      if(flag) {
        print(cbind(a, b, c)) # [a, b, c] in MATLAB
      }
    }
  }
}

# library("schoolmath") # for function 'gcd' - prints "n is a prime!" several times per iteration and is VERY slow!

# https://answers.yahoo.com/question/index?qid=20120125211736AA32hEy

GCD <- function(a, b) { 
  if(b == 0) { 
    value <- a 
    return(value)
  } else { 
    value <- GCD(b, a %% b) # '%%' in R = mod(a, b) in MATLAB
    return(value)
  }
}

find_triples9 <- function(n) {
  for(a in 1:n) {
    for(b in a:n) {
      if(GCD(a, b) > 1) {
        next # 'continue' in MALAB
      }
      c <- hypotenuse(a, b)
      if(is.integral(c)) {
        print(cbind(a, b, c)) # [a, b, c] in MATLAB
      }
    }
  }
}
