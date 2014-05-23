function res = find_triples7()
    for a = 1:3
        for b = a:4
            c = hypotenuse(a, b);
            flag = isintegral(c);
            if flag
                [a, b, c]
            end
        end
    end
end
