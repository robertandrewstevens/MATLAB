function res = find_triples8 (n)
    for a = 1:n
        for b = a:n
            c = hypotenuse(a, b);
            flag = isintegral(c);
            if flag
                [a, b, c]
            end
        end
    end
end
