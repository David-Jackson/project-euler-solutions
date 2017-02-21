def primeSieve(n):
  l = [True] * (n + 1)
  for i in range(2, int(n**0.5) + 1):
    if l[i]:
      for j in range(i**2, n + 1, i):
        l[j] = False
  res = []
  for i in range(2, n):
    if l[i]:
      res.append(i)
  return res

def circular(n):
  original = n
  length = 0
  while n >= 1:
    n /= 10
    length += 1
  n = original
  for i in range(length):
    x = n % 10
    n /= 10
    n += (x * int(10**(length-1)))
    yield n

primes = primeSieve(1000000)
print "Generated {0} Primes".format(len(primes))
circPrimes = []

for x in primes:
  print "{0}\r".format(x),
  newPrimes = []
  for circle in circular(x):
    if circle in primes:
      newPrimes.append(circle)
    else:
      newPrimes = []
      break
  circPrimes += newPrimes
print
res = []
for x in circPrimes:
  if x not in res:
    res.append(x)
print len(res)