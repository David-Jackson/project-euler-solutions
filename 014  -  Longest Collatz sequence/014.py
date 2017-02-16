def collatzSeqLen(n):
  seq = 0
  while (n > 1):
    if (n % 2 == 0):
      n /= 2
    else:
      n *= 3
      n += 1
    seq += 1
  return seq

max = 0
maxI = 0

for i in range(int(1E6)):
  c = collatzSeqLen(i)
  if (c > max):
    max = c
    maxI = i
  print "{0}\r".format(i),
print

print "Answer:", maxI