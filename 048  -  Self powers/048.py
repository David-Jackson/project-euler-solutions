sum = 0

for i in range(1, 1001):
    sum += (i**i)

print "Answer:", sum % int(1E10)
