# Digit fifth powers


def split(x):
  res = []
  while x > 0:
    res.append(x % 10)
    x = int(x / 10)
  return res

def sum5pow(arr):
  sum = 0
  for x in arr:
    sum = sum + pow(x, 5)
  return sum

def sum4pow(arr):
  sum = 0
  for x in arr:
    sum = sum + pow(x, 4)
  return sum

i = 2
x = 0

while i < 1000000:
  i = i + 1
  #print i
  digits = split(i)
  if (i == sum5pow(digits)):
    x = x + i
    print x
  

print "Answer:", x