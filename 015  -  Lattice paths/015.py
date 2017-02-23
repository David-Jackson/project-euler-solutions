def pascal_triangle(n):
    tri = [[1]]
    while (len(tri) < n):
        prev = [0] + tri[-1] + [0]
        a = []
        for i in range(len(prev)-1):
            a.append(prev[i] + prev[i+1])
        tri.append(a)
    return tri[-1]


def lattice_path(n):  # solution for n x n square
    return max(pascal_triangle((n*2) + 1))


print "Answer:", lattice_path(20)
