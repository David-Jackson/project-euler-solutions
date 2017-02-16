
def reverseNum(x):
  s = str(x)
  return int("".join(reversed(s)))

def isPalendrome(x):
  s = str(x)
  return s == "".join(reversed(s))

def isLychrel(x):
  iter = 0
  while iter < 50:
    x = x + reverseNum(x)
    if isPalendrome(x):
      return False
    iter = iter + 1
  return True


count = 0

for i in range(10000):
  if isLychrel(i):
    count = count + 1

print "Answer:", count