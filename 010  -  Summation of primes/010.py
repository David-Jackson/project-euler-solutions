#Sieve of Eratosthenes implementation

def sumPrimeSieve(n):
  l = [True] * (n + 1)
  for i in range(2, int(n**0.5) + 1):
    if l[i]:
      for j in range(i**2, n + 1, i):
        l[j] = False
  sum = 0
  for i in range(2, n):
    if l[i]:
      sum += i
  return sum



print sumPrimeSieve(int(2E6))

