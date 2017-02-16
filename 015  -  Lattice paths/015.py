def pascalTriangle(n):
  tri = [[1]]
  while (len(tri) < n):
    prev = [0] + tri[-1] + [0]
    a = []
    for i in range(len(prev)-1):
      a.append(prev[i] + prev[i+1])
    tri.append(a)
  return tri[-1]

def latticePath(n): # solution for n x n square
  return max(pascalTriangle((n*2) + 1))

print "Answer:", latticePath(20)