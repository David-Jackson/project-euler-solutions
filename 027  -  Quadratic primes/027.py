
def solve(n, a, b):
  return (n * n) + (a * n) + b

def isPrime(n):
  if (n <= 0):
    return False
  if (n <= 3):
    return True
  limit = int(n**(.5))
  for i in range(2, limit + 1):
    if (n % i == 0):
      return False
  return True

def sequenceOfPrimes(a, b):
  index = 0
  while (True):
    if isPrime(solve(index, a, b)):
      index = index + 1
    else:
      break
  return index


def findMaxPrimeSequence(): 
  max = 0
  maxA = 0
  maxB = 0

  a = -999

  while (a < 1000):
    b = -1000
    while (b <= 1000):
      seq = sequenceOfPrimes(a, b)
      if (seq > max):
        max = seq
        maxA = a
        maxB = b
      b = b + 1
    a = a + 1
    print '{0}%\r'.format((a+1000)/20),
  print
  return (maxA * maxB)


ans = findMaxPrimeSequence()
print "Answer:", ans