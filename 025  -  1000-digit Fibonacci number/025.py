thou = 10**999

f0 = 0
f1 = 1
f2 = 1
index = 2

while long(f2) < thou:
    f0 = f1
    f1 = f2
    f2 = f0 + f1
    index = index + 1

print "Answer:", index
