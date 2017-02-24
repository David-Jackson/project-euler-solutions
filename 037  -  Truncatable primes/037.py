# Sieve of Eratosthenes implementation
def prime_sieve(n):
    l = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if l[i]:
            for j in range(i**2, n + 1, i):
                l[j] = False
    return l


def trunc_right(n):
    trunc = []
    while n > 0:
        trunc.append(n)
        n /= 10
    return trunc


def trunc_left(n):
    trunc = []
    div = 10
    mod = 0
    while mod != n:
        mod = n % div
        div *= 10
        trunc.append(mod)
    return trunc


sum = 0
primes = prime_sieve(1000000)
primes[1] = False

for i in range(10, len(primes)):
    prime = primes[i]
    if (prime):
        all_prime = True
        truncs = trunc_left(i) + trunc_right(i)
        for t in truncs:
            if (not primes[t]):
                all_prime = False
                break
        if (all_prime):
            sum += i

print "Answer:", sum
