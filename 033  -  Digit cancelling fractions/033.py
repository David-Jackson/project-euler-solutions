def digits(n):
    res = []
    while n > 0:
        res.append(n % 10)
        n /= 10
    return res


def find_common(n1, n2):
    res = []
    arr1 = digits(n1)
    arr2 = digits(n2)
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            res.append([i, arr2.index(arr1[i])])
    return res


def fract_prod(arr):
    nump = 1
    denp = 1
    for fract in arr:
        nump *= fract[0]
        denp *= fract[1]
    return [nump, denp]


def gcd(fract):
    a = fract[0]
    b = fract[1]
    while b:
        a, b = b, a % b
    return a


def reduce(fract):
    fact = gcd(fract)
    return [fract[0]/fact, fract[1]/fact]


num = 11
den = 11

answers = []

while den < 100:
    while num < den:
        numd = digits(num)
        dend = digits(den)
        for group in find_common(num, den):
            test_n = numd[0]
            if group[0] == 0:
                test_n = numd[1]
            test_d = dend[0]
            if group[1] == 0:
                test_d = dend[1]
            if (
                test_d != 0 and 
                (1.0 * test_n / test_d) == (1.0 * num / den) and 
                numd[group[0]] != 0 and dend[group[1]] != 0
            ):
                answers.append([num, den])
        num += 1
    num = 11
    den += 1

fract = reduce(fract_prod(answers))
print "Answer:", fract[1]
