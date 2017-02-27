def tri_solutions(p):
    solutions = 0
    for a in range(1, p/3):
        for b in range(1, p-a):
            c = p - a - b
            if (a**2 + b**2) == c**2:
                solutions += 1
    return solutions


max_p = 0
max = 0

for p in range(3, 1001):
    s = tri_solutions(p)
    if s > max:
        max_p = p
        max = s
        

print "Answer:", max_p
