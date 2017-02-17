
def primeSieve(n):
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


primes = primeSieve(int(1E6))

cSum = 0
max = 0
maxLength = 0

for a in range(len(primes)):
  for b in range(a + maxLength, len(primes)):
    cSum = sum(primes[a:b])
    if cSum > 1E6:
      break
    if cSum in primes and b - a > maxLength:
      max = cSum
      maxLength = b - a


print "Answer:", max