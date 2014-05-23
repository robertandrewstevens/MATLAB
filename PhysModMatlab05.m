% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 5:  Functions

echo on

% 5.1 Name Collisions

A1 = 1;
total = 0;
for i = 1:10
    a = A1 * 0.5^(i - 1);
    total = total + a;
end
ans = total

% 5.2 Functions

% create file "myfunc.m"

myfunc(1)

y = myfunc(1)

clear
y = myfunc(1);
who
%s - comment out to avoid intentional error

s = 1;
c = 1;
y = myfunc(1);
s, c

% 5.3 Documentation

% Add 3 lines of comments to beginning of 'myfunc.m'

help myfunc

% 5.4 Function names

% If change 'myfunc.m' to
% function res = something_else (x)
%    s = sin(x);
%    c = cos(x);
%    res = abs(s) + abs(c);
% end

y = myfunc(1);
%y = something_else(1); % comment out intentional error

%y = my func(1) % comment out intentional error

sum(1:3)
sum

% 5.5 Multiple input variables

c = hypotenuse(3, 4)

%c = hypotenuse(3) % comment out intentional error

%c = hypotenuse(3, 4, 5) % comment out intentional error

% 5.6 Logical functions

isprime(17)
isprime(21)

c = hypotenuse(3, 4)
isinteger(c)

% create file "isintegral.m"
isintegral(c)

% 5.7 An incremental development example

find_triples1

find_triples2

% 5.8 Nested loops

find_triples3

find_triples4

find_triples5

% 5.9 Conditions and flags

find_triples6

find_triples7

% 5.10 Encapsulation and generalization

find_triples7()

find_triples8(15)

% 5.11 A misstep

% If change 'hypotenuse.m' to
% function res = hypotenuse(a, b, d)
%    res = (a.^d + b.^d) ^ (1/d);
% end

%find_triples8(20) % comment out intentional error

% 5.12 continue

find_triples9(40)

% 5.13 Mechanism and leap of faith - no code in this section

echo off
