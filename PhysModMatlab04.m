% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 4:  Vectors

echo on

% 4.1 Checking preconditions

n = -1

A1 = 1;
total = 0;
for i = 1:n
    a = A1 * 0.5^(i - 1);
    total = total + a;
end
ans = total

1:-1

% 4.2 if

if n < 0
    ans = NaN
end

if n < 0
    ans = NaN
else
    A1 = 1;
    total = 0;
    for i = 1:n
        a = A1 * 0.5^(i - 1);
        total = total + a;
    end
    ans = total
end

% 4.3 Relational operators

x = 5;
x < 10

flag = x > 10

%if x = 5 % comment out intentional error so script runs

% 4.4 Logical operators

x = 5;
0 < x < 10 % right for the wrong reason

x = 17
0 < x < 10 % just plain wrong

ans = 0
if 0 < x
    if x < 10
        ans = 1
    end
end

x = 5;
0 < x && x < 10

x = 17;
0 < x && x < 10

% 4.5 Vectors

X = 1:5

% 4.6 Vector arithmetic

Y = X + 5

Z = X + Y

W = 1:3

%X + W % comment out intentional error so script runs

% 4.7 Everything is a matrix

scalar = 5

vector = 1:5

matrix = ones(2,3)

whos

X = 1:5

Y = 1:5

%Z = X*Y % comment out intentional error so script runs

X .* Y

% 4.8 Indices

Y = 6:10

Y(1)

Y(5)

i = 1;

Y(i + 1)

for i =  1:5
    Y(i)
end

for i = 1:length(Y)
    Y(i)
end

% 4.9 Indexing errors

%Y(0) % comment out intentional error so script runs

%Y(6) % comment out intentional error so script runs

%Y(1.5) % comment out intentional error so script runs

% 4.10 Vectors and sequences

n = 10;
F(1) = 1;
F(2) = 1;
for i = 3:n
    F(i) = F(i - 1) + F(i - 2);
end
ans = F(n)

F(1) = 1;
F(2) = 1;
for i = 1:n - 2
    F(i + 2) = F(i + 1) + F(i);
end
ans = F(n)

% 4.11 Plotting vectors

plot(F)

X = 1:5
Y = 6:10
plot(X, Y)

% 4.12 Reduce

total = 0;
for i = 1:length(X)
    total = total + X(i);
end
ans = total

% 4.13 Apply

X = 1:5 % redefine so example runs as intended (?)
for i = 1:length(X)
    Y(i) = X(i)^2;
end
Y

% 4.14 Search

X = 10:-1:-10

for i = 1:length(X)
    if X(i) == 0
        ans = i
    end
end

for i = 1:length(X)
    if X(i) == 0
        ans = i
        break
    end
end

X = linspace(1, 2);
echo off
for i = 1:length(X)
    Y(i) = sin(X(i));
end
echo on
plot(X, Y)

echo off
for i = 1:length(Y)
    if Y(i) == 0.9
        ans = i
        break
    end
end
echo on

% 4.15 Spoiling the fun

X = 1:5 % redefine so example runs as intended (?)
Y = X .^ 2

X = linspace(0, 2*pi);
Y = sin(X);
plot(X, Y)
