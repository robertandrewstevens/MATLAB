% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 1:  Variables and values

echo on

% 1.1 A glorified calculator

2 + 1

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9

2*3 - 4/5

2 * (3 - 4) / 5

2^16

% 1.2 Math functions

sin(1)

atan2(1,1)

exp(1)

log(exp(3))

sqrt(sin(0.5)^2 + cos(0.5)^2)

% 1.3 Documentation

help sin

%SIN(1) % comment out so script completes without (intentional) error

% 1.4 Variables

pi

pi * 3^2

sin(pi/2)

exp(i * pi)

3^2 + 4^2

sqrt(ans)

% 1.5 Assignment statements

x = 6 * 7

fibanocci0 = 1;

LENGTH = 10;

first_name = 'allen'

% 1.6 Why variables?

e = exp(1)

r = 3

area = pi * r^2

theta = 0 % define to avoid error message
sigma = 1 % define to avoid error message
zeta = 0 % define to avoid error message

ans = ((x - theta) * sqrt(2 * pi) * sigma) ^ -1 * ...
    exp(-1/2 * (log(x - theta) - zeta)^2 / sigma^2)

shiftx = x - theta
demon = shiftx * sqrt(2 * pi) * sigma
temp = (log(shiftx) - zeta) / sigma
exponent = -1/2 * temp^2
ans = exp(exponent) / demon

% 1.7 Errors

area = pi * r^2 % corrected "area = pi r^2"

sin(1) * pi % corected "sin pi"

abs(pi) % corrected "abs pi"

1 / 2 * sqrt(pi)

1/ (2 * sqrt(pi))

% 1.8 Floating-point arithmetic

1/3

format long
1/3

factorial(100)

speed_of_light = 3.0e8

realmax

realmin

factorial(170)

factorial(171)

1/0

0/0

% 1.9 Comments

speed_of_light = 3.0e8 % meters per second

x = 5 % assign the value 5 to x (avoid this type of comment)

p = 0    % postion from the origin in meters
v = 100  % velocity in meters / second
a = -9.8 % acceleration of gravity in meters / second^2

