def collatz_seq_len(n):
    seq = 0
    while (n > 1):
        if (n % 2 == 0):
            n /= 2
        else:
            n *= 3
            n += 1
        seq += 1
    return seq


max = 0
max_i = 0

for i in range(int(1E6)):
    c = collatz_seq_len(i)
    if (c > max):
        max = c
        max_i = i
    print "{0}\r".format(i),

print "Answer:", max_i
