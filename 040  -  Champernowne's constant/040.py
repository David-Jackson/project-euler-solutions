n = 1
prod = 1
string = ""
i = 0

while n <= 1000000:
    while len(string) < n + 1:
        string += str(i)
        i += 1
    prod *= int(string[n])
    n *= 10

print "Answer:", prod
