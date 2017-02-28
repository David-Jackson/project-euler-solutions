sum = 1

for i in range(3, 1001 + 1, 2):
    sqr = i ** 2
    for j in range(4):
        sum += sqr
        sqr -= (i - 1)

print "Answer:", sum
