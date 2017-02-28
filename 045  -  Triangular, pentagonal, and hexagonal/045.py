def gen_tri(arr, limit = -1):
    if limit == -1:
        limit = arr[-1] + 1
    n = len(arr) + 1
    while arr[-1] < limit:
        arr.append(int((0.5 * n) * (n + 1)))
        n += 1


def gen_pent(arr, limit = -1):
    if limit == -1:
        limit = arr[-1] + 1
    n = len(arr) + 1
    while arr[-1] < limit:
        arr.append(int((0.5 * n) * ((3 * n) - 1)))
        n += 1


def gen_hex(arr, limit = -1):
    if limit == -1:
        limit = arr[-1] + 1
    n = len(arr) + 1
    while arr[-1] < limit:
        arr.append(n * ((2 * n) - 1))
        n += 1


tri = [1]
pent = [1]
hex = [1]

count = 0

while count < 2:
    gen_tri(tri)
    while tri[-1] not in pent or tri[-1] not in hex:
        gen_tri(tri)
        gen_pent(pent, tri[-1])
        gen_hex(hex, tri[-1])
    count += 1


print "Answer:", tri[-1]
