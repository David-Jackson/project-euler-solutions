ITERATION_LIMIT = 1000


def reciprocal_cycles(x):
    iterations = 0

    length = 0
    history = []

    num = 1
    den = x
    while (num != 0 or iterations < ITERATION_LIMIT):
        if (num < den):
            num *= 10
        num = num % den
        if (num in history):
            length = len(history) - history.index(num)
            break
        history.append(num)

    if (iterations >= ITERATION_LIMIT):
        print "Iteration break"

    return length


def solve():
    i = 2
    max = 0
    maxI = 0
    while (i < 1000):
        obj = reciprocal_cycles(i)
        if (obj > max):
            max = obj
            maxI = i
        i += 1
    print "Answer: {0}. \
            1/{0} has a {1}-digit recurring cycle".format(maxI, max)
    return maxI


solve()
