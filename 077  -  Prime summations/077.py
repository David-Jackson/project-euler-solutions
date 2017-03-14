# Sieve of Eratosthenes implementation
def prime_sieve(n):
    primes = []
    l = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if l[i]:
            for j in range(i**2, n + 1, i):
                l[j] = False
    for i in range(2, n):
        if l[i]:
            primes.append(i)
    return primes


amount = 100

# Generate a list of prime numbers
nums = prime_sieve(amount)

ways = [0] * (amount + 1)
ways[0] = 1

for num in nums:
    for j in range(num, amount + 1):
        ways[j] += ways[j - num]

for i in range(len(ways)):
    if ways[i] > 5000:
        print "Answer:", i
        break
