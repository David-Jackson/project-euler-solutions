
def product(arr):
  res = 1
  for i in arr:
    res *= i
  return res

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


json_list = [{'n':1,'rad':'1'}]

for i in range(2, 100001):
  json_list.append({
    'n': i,
    'rad': product(distinctPrimeFactors(i))
  })
  if (i % 1000 == 0):
    print "{0}\r".format(i),
print



sorted_list = sorted(json_list, key=lambda k: (int(k['rad']),int(k['n'])))

print "Answer:", sorted_list[9999]['n']