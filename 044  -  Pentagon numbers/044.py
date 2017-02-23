

# generate pentagonial number
def get_pent(x):
    return x * ((3 * x) - 1) / 2


# return the inverse of a pentagonial number
def rev_pent(x):
    return (((24 * x) + 1) ** 0.5 + 1) / 6


# check if a number is pentagonial
def is_pent(x):
    if x == 0:
        return False
    y = rev_pent(x)
    return y / int(y) == 1


pent = [1]


# generate a list of pentagonial numbers into the array pent
def generate_pent_nums(x):
    for i in range(len(pent), x):
        pent.append(get_pent(i))


# index
a = 1

# continue boolean
cont = True

while (cont):
    a = a + 1
    generate_pent_nums(a)
    c = pent[len(pent)-1]
    # traverse the list backwards to minimize c - d
    for d in reversed(pent):
        if (is_pent(c + d) and is_pent(c - d)):
            print "Answer:", c - d
            cont = False
            break
