def teen_sum(a, b, c):
    def fix_teen(n):
        return 0 if 13 <= n <= 19 and n != 15 and n != 16 else n

    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)

    total = a + b + c
    print(f"Sum = {total}")

# Sample Runs
teen_sum(3, 1, 4)
teen_sum(21, 1, 2)
teen_sum(13, 1, 19)
