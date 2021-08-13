prices = [7,1,5,3,6,4]


max_profit = 0
min = prices[0]

for i in prices:
    if i > minprice:
        maxprofit += i-minprice
        minprice = i
    else:
        minprice = i

print(max_profit)