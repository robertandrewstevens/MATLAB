% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 3:  Loops
% 3.8 Generalization

echo off

A1 = 1;
total = 0;
for i = 1:n % instead of "for i = 1:10"
    a = A1 * 0.5^(i - 1);
    total = total + a;
end
ans = total

echo on
