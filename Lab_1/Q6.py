def fix_teen(a, b, c):
    def fix_teen_value(n):
        if n in range(13, 20) and n != 15 and n != 16:
            return 0
        return n

    a = fix_teen_value(a)
    b = fix_teen_value(b)
    c = fix_teen_value(c)

    return a + b + c

# Sample runs
print("Input: a=3, b=1, c=4   ; Output:", fix_teen(3, 1, 4))
print("Input: a=21, b=1, c=2  ; Output:", fix_teen(21, 1, 2))
print("Input: a=13, b=1, c=19 ; Output:", fix_teen(13, 1, 19))
