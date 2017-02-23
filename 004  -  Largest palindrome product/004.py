LOWER_LIMIT = 100
UPPER_LIMIT = 1000


def num_to_arr(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n /= 10
    return arr


def reverse(arr):
    res = []
    for i in reversed(arr):
        res.append(i)
    return res


def is_palindromic(n):
    a = num_to_arr(n)
    return a == reverse(a)


ans = 0
for a in range(LOWER_LIMIT, UPPER_LIMIT):
    for b in range(LOWER_LIMIT, UPPER_LIMIT):
        p = a * b
        if (is_palindromic(p)):
            ans = max(ans, p)

print "Answer:", ans
