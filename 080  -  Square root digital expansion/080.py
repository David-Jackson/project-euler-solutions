from decimal import Decimal, getcontext

getcontext().prec = 102


def sum_100_dec(n):
    sum = 0
    for i in range(100):
        n_int = int(n)
        n -= n_int
        n *= 10
        sum += n_int
    return sum


total = 0

for i in range(1, 100 + 1):
    sqrt = Decimal(i).sqrt()
    if int(sqrt) != sqrt:
        total += sum_100_dec(sqrt)

print "Answer:", total
