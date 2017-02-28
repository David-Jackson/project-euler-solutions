def gen_tri(arr, limit):
    n = len(arr)
    while arr[-1] < limit:
        arr.append(int((0.5 * n) * (n + 1)))
        n += 1

alpha = '"ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tri = [1]

with open("p042_words.txt") as f:
    words = f.read().split(",")

total = 0

for word in words:
    score = 0
    for l in word:
        score += alpha.find(l)
    if score > tri[-1]:
        gen_tri(tri, score)
    if score in tri:
        total += 1


print "Answer:", total
