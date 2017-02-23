def solve(n, a, b):
    return (n * n) + (a * n) + b


def is_prime(n):
    if (n <= 0):
        return False
    if (n <= 3):
        return True
    limit = int(n**(.5))
    for i in range(2, limit + 1):
        if (n % i == 0):
            return False
    return True


def sequence_of_primes(a, b):
    index = 0
    while (True):
        if is_prime(solve(index, a, b)):
            index = index + 1
        else:
            break
    return index


def find_max_prime_sequence():
    max = 0
    max_a = 0
    max_b = 0

    a = -999

    while (a < 1000):
        b = -1000
        while (b <= 1000):
            seq = sequence_of_primes(a, b)
            if (seq > max):
                max = seq
                max_a = a
                max_b = b
            b = b + 1
        a = a + 1
        print '{0}%\r'.format((a+1000)/20),
    print
    return (max_a * max_b)


ans = find_max_prime_sequence()
print "Answer:", ans
