coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
ways = [0] * (amount + 1)
ways[0] = 1

for coin in coins:
    for j in range(coin, amount + 1):
        ways[j] += ways[j - coin]

print "Answer:", ways[amount]
