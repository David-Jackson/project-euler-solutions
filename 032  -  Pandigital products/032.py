def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True


def arr_to_int(arr):
    res = 0
    for n in arr:
        res *= 10
        res += n
    return res


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

products = []

while next_permutation(arr):
    prod = arr_to_int(arr[0:2]) * arr_to_int(arr[2:5])
    if prod == arr_to_int(arr[5:9]) and prod not in products:
        products.append(prod)
    prod = arr_to_int(arr[0:1]) * arr_to_int(arr[1:5])
    if prod == arr_to_int(arr[5:9]) and prod not in products:
        products.append(prod)

print "Answer:", sum(products)
