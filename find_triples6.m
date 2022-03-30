function res = find_triples6()
    for a = 1:3
        for b = a:4
            c = hypotenuse(a, b);
            flag = isintegral(c);
            [c, flag]
        end
    end
end
