def reverse_num(x):
    s = str(x)
    return int("".join(reversed(s)))


def is_palendrome(x):
    s = str(x)
    return s == "".join(reversed(s))


def is_lychrel(x):
    iter = 0
    while iter < 50:
        x = x + reverse_num(x)
        if is_palendrome(x):
            return False
        iter = iter + 1
    return True


count = 0

for i in range(10000):
    if is_lychrel(i):
        count = count + 1

print "Answer:", count
