def factors(x):
    f = [1]
    for i in range(2, int(x**0.5) + 1):
        if (x % i == 0):
            f.append(i)
            if (x / i not in f):
                f.append(x / i)
    return f


def is_abundant(n):
    return sum(factors(n)) > n


UPPER_LIMIT = 28123

nums = [False] * (UPPER_LIMIT + 1)
ab_nums = []

for i in range(2, len(nums)):
    if is_abundant(i):
        ab_nums.append(i)

for a in ab_nums:
    for b in ab_nums:
        sum = a + b
        if (sum > UPPER_LIMIT):
            break
        nums[sum] = True

sum = 0

for i in range(len(nums)):
    if not nums[i]:
        sum += i


print "Answer:", sum
