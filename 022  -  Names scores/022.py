alpha = '"ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open("p022_names.txt") as f:
    names = f.read().split(",")

names.sort()

total = 0

for i in range(len(names)):
    name = names[i]
    score = 0
    for l in name:
        score += alpha.find(l)
    score *= (i + 1)
    total += score


print "Answer:", total
