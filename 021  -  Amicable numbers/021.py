

# sum_factors returns the sum of factors not including x
def sum_factors(x):
    sum = 1
    for i in range(2, int(x**0.5) + 1):
        if (x % i == 0):
            sum += i
            if (i != x / i):
                sum += (x / i)
    return sum


n = 1

amicables = []

while n < 10000:
    dn = sum_factors(n)
    if n != dn and n == sum_factors(dn) and n not in amicables:
        amicables.append(n)
        amicables.append(dn)
    n += 1

print "Answer:", sum(amicables)
