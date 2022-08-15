prices = list(map(int, input().split()))
min_price = prices[0]
max_price = prices[0]

for i in range(1, len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    elif prices[i] > max_price:
        max_price = prices[i]