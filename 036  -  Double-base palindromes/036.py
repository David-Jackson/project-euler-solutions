def reverse_int(n):
    rev = 0
    while n > 0:
        rev *= 10
        rev += n % 10
        n /= 10
    return rev


def reverse_str(s):
    rev = ""
    for l in s:
        rev = l + rev
    return rev


def to_bin(n):
    return "{0:b}".format(n)


def base10_palindrome(n):
    return n == reverse_int(n)


def base2_palindrome(n):
    bin = to_bin(n)
    return bin == reverse_str(bin)


sum = 0

for i in range(1, 1000000):
    if (base10_palindrome(i)):
        if (base2_palindrome(i)):
            sum += i

print "Answer:", sum
