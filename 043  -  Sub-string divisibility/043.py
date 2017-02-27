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


def is_special(arr):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(len(primes)):
        if arr_to_int(arr[i+1:i+4]) % primes[i] != 0:
            return False
    return True


arr = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

while next_permutation(arr):
    if is_special(arr):
        sum += arr_to_int(arr)

print "Answer:", sum

