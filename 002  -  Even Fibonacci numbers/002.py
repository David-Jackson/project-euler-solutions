sum = 0

f0 = 1
f1 = 1
f2 = 1

while f2 < 4000000:
  f0 = f1
  f1 = f2
  f2 = f1 + f0
  if f2 % 2 == 0: 
    sum = sum + f2


print "Answer:", sum