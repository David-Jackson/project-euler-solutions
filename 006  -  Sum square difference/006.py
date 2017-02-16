
sumSquare = 0
squareSum = 0

for i in range(1,101):
  sumSquare += i**2
  squareSum += i

squareSum = squareSum**2

print "Answer:", squareSum - sumSquare