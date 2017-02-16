nums = []

with open("numbers.txt", "r") as f:
  nums = f.read().split("\n")

for i in range(len(nums)):
  nums[i] = long(nums[i])

sum = sum(nums)

while (sum > 1E10):
  sum /= 10


print "Answer:", int(sum)