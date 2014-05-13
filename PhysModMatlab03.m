% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 3:  Loops

echo on

% 3.1 Updating variables - No code in section

% 3.2 Kinds of error - No code in section

% 3.3 Absolute and relative error - No code in section

% 3.4 for loops

echo off
a = 150;
b = 150;
for i = 1:52
    carUpdate % renamed from "car_update"
end
echo on

1:5

echo off
for i = 1:5
    i
end
echo on

% 3.5 plotting

plot(1, 2)

plot(1, 2, 'o')

plot(1, 2, 'ro')

hold on
plot(1, 1, 'o')
plot(2, 2, 'o')

% 3.6 Sequences

a = 1
for i = 2:10
    a = a/2
end

% 3.7 Series

A1 = 1;
total = 0;
for i = 1:10
    a = A1 * 0.5^(i - 1);
    total = total + a;
end
ans = total

% 3.8 Generalization

% modify script "series.m" from Exercise 3.4

format long

n = 10; seriesV2
n = 20; seriesV2
n = 30; seriesV2
n = 40; seriesV2
