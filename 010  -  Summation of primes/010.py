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

sum = 0

for i in range(1, int(2E6)):
  if (isPrime(i)):
    sum += i
  print "{0}\r".format(i),
print

print "Answer:", sum
