
# generate pentagonial number
def getPent(x):
  return x * ((3 * x) - 1) / 2

# return the inverse of a pentagonial number
def revPent(x):
  return (((24 * x) + 1) ** 0.5 + 1) / 6

# check if a number is pentagonial
def isPent(x):
  if x == 0:
    return False
  y = revPent(x)
  return y / int(y) == 1



pent = [1]
# generate a list of pentagonial numbers into the array pent
def generatePentNums(x):
  for i in range(len(pent), x):
    pent.append(getPent(i))

# index
a = 1

# continue boolean
cont = True

while (cont): 
  a = a + 1
  generatePentNums(a)
  c = pent[len(pent)-1]
  # traverse the list backwards to minimize c - d
  for d in reversed(pent):
    if (isPent(c + d) and isPent(c - d)):
      print "Answer:", c - d
      cont = False
      break

