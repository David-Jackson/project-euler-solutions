import math

r = 1.0
l_sect = ((2 * r * 2 * r) - (math.pi * r * r)) / 4


def solve_for_x(n): 
    # find the x coordinate where the line between the
    # lower left corner of the 1st sqaure and the upper
    # right corner of thenth square intersects with the
    # circle in the 1st square
    n = 1.0 * n
    return ((2 + (2 / n)) - math.sqrt(((-2 - (2 / n)) ** 2) - (4 + (4/(n * n))))) / (2 * (1 + (1 / (n * n))))


def solve_for_y(x, n):
    # find the y coordinate where the line between the
    # lower left corner of the 1st sqaure and the upper
    # right corner of thenth square intersects with the
    # circle in the 1st square
    return (1.0 / n) * x


def div_sect(n): 
    # find the area of the segment
    x = solve_for_x(n)
    y = solve_for_y(x, n)

    tri_area = 0.5 * r * y

    c = math.hypot(y, 1.0 - x)
    theta = 2.0 * math.asin(c / (2.0 * r))

    arc_area = (r / 2.0) * (theta - math.sin(theta))

    return tri_area - arc_area


n = 1
while (True):
    ratio = div_sect(n) / l_sect
    print "{0} - {1}\r".format(n, ratio),
    if ratio < 0.001:
        break
    n += 1

print
print "Answer:", n