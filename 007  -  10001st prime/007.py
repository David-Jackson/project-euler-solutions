

def is_prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    limit = int(n**(.5))
    for i in range(2, limit + 1):
        if (n % i == 0):
            return False
    return True

i = 1
i_prime = 2
n = 3

while (i < 10001):
    if (is_prime(n)):
        i += 1
        i_prime = n
    n += 2


print "Answer:", i_prime
