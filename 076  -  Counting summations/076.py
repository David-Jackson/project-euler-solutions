nums = []
amount = 100
for i in range(1, amount):
    nums.append(i)
ways = [0] * (amount + 1)
ways[0] = 1

for num in nums:
    for j in range(num, amount + 1):
        ways[j] += ways[j - num]

print "Answer:", ways[amount]
