
with open("triangle.txt") as f:
    tri = [map(int, line.split()) for line in f]

for row_index in range(len(tri)-2, -1, -1):
    row = tri[row_index]
    for index in range(len(row)):
        node = row[index]
        tri[row_index][index] = (
            node + max(
                tri[row_index + 1][index],
                tri[row_index + 1][index + 1]
            )
        )

print "Answer:", tri[0][0]
