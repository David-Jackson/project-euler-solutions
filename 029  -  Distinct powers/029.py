res = []

for a in range(2, 101):
  for b in range(2, 101):
    p = a ** b
    if (p not in res):
      res.append(p)

print "Answer:", len(res)