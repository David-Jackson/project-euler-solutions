arr = []

with open("digits.txt") as f:
    for line in f:
        arr = arr + [int(x) for x in line.strip()]


def prod(a):
    res = 1
    for x in a:
        res *= x
    return res


res = 0
for i in range(0, len(arr)-12):
    res = max(res, prod(arr[i:i+13]))


print "Answer:", res
