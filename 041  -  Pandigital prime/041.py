def is_prime(_n):
    _is_prime = True
    _sqrt = _n ** 0.5
    for i in range(2, int(_sqrt) + 1):
        if _n % i == 0:
            _is_prime = False
            break
    return _is_prime


def arr_to_int(arr):
    res = 0
    for n in arr:
        res *= 10
        res += n
    return res


# This is a REVERSE lex. permutation generator
def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] >= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True


og_arr = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = og_arr[:]
count = 0

while len(arr) > 3:
    og_arr = og_arr[1:]
    arr = og_arr[:]
    while next_permutation(arr):
        count += 1
        x = arr_to_int(arr)
        print "{0}\r".format(x),
        if is_prime(x):
            print "Answer:", x
            arr = []
            break
            
