% Physical Modeling in MATLAB by Allen B. Downey
% Chapter 4:  Vectors
% Exercise 4.4 

% Write a loop that finds the index of the first negative number in
% a vector and stores it in ans. 
% If there are no negative numbers, it should set ans to -1 (which is 
% not a legal index, so it is a good way to indicate the special case).

%echo on

X = linspace(0, 2*pi);
for i= 1:length(X)
    Y(i) = sin(X(i));
end
plot(X, Y);

ans = -1;
for i = 1:length(Y)
    if Y(i) < 0
        ans = i;
        break;
    end
end
ans

X = linspace(0, pi); % check when no negative numbers
for i= 1:length(X)
    Y(i) = sin(X(i));
end
plot(X, Y);

ans = -1;
for i = 1:length(Y)
    if Y(i) < 0
        ans = i;
        break;
    end
end
ans

%echo off
