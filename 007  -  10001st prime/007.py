

def isPrime(n):
  if (n <= 1):
    return False
  if (n <= 3):
    return True
  limit = int(n**(.5))
  for i in range(2, limit + 1):
    if (n % i == 0):
      return False
  return True

i = 1
iPrime = 2
n = 3

while (i < 10001):
  if (isPrime(n)):
    i += 1
    iPrime = n
  n += 2


print "Answer:", iPrime