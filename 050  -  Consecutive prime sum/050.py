def prime_sieve(n):
    l = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if l[i]:
            for j in range(i**2, n + 1, i):
                l[j] = False
    primes = []
    for i in range(2, n):
        if l[i]:
            primes.append(i)
    return primes


primes = prime_sieve(int(1E6))

c_sum = 0
max = 0
max_length = 0

for a in range(len(primes)):
    for b in range(a + max_length, len(primes)):
        c_sum = sum(primes[a:b])
        if c_sum > 1E6:
            break
        if c_sum in primes and b - a > max_length:
            max = c_sum
            max_length = b - a


print "Answer:", max
