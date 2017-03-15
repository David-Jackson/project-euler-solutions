def fact(n):
    if (n <= 1):
        return 1
    return n * fact(n-1)


facts = [fact(i) for i in range(10)]


def fact_digits(n):
    res = 0
    while n > 0:
        res += facts[n % 10]
        n /= 10
    return res


sum = 0

for i in range (10, 50000):
   if i == fact_digits(i):
       sum += i

print "Answer:", sum
