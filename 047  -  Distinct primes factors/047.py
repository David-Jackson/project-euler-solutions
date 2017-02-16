
REQ_FACTOR_LENGTH = 4
REQ_STREAK = 4

curStreak = 0
n = 3


def distinctPrimeFactors(n):
  d = 2
  res = []
  while n > 1:
    if (n % d == 0):
      if (d not in res):
        res.append(d)
      n /= d
      d -= 1
    d += 1
  return res


while (curStreak < REQ_STREAK):
  if (len(distinctPrimeFactors(n)) == REQ_FACTOR_LENGTH):
    curStreak += 1
  else:
    curStreak = 0
  n += 1
  if (n % 1000 == 0):
    print "{0}\r".format(n),
print

for i in range(n - REQ_STREAK, n):
  print i, "-", distinctPrimeFactors(i)

print "Answer:", n - REQ_STREAK