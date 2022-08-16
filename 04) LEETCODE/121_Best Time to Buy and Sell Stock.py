prices = list(map(int, input().split()))

buy_price = prices[0]
max_profit = 0

for i in range(len(prices)):
    if prices[i] < buy_price:
        buy_price = prices[i]

    else:
        if prices[i] - buy_price > max_profit:
            max_profit = max(max_profit, prices[i] - buy_price)

print(max_profit)