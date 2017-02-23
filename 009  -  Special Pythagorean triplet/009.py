def pythag_triplet():
    for a in range(1, 999):
        for b in range(1000 - a):
            c = 1000 - a - b
            if (a**2 + b**2 == c**2):
                return a * b * c


print "Answer:", pythag_triplet()
