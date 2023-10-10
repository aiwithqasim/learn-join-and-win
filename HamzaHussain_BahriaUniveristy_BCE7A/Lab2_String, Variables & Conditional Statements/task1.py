def fix_teen(n):

    if 13 <= n <= 19:
        return 0
    else:
        return n


def sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)

    total = a + b + c
    return total


print("Input: a=3, b=1, c=4")
print("Output: Sum =", sum(3, 1, 4))

print("Input: a=21, b=1, c=2")
print("Output: Sum =", sum(21, 1, 2))

print("Input: a=13, b=1, c=19")
print("Output: Sum =", sum(13, 1, 19))
