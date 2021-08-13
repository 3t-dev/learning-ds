prices = [7,1,5,3,6,4]

min = prices(0)
max = 0
max_profit = 0
for i in len(prices):
	if prices(i) > min:	
		profit = prices(i) - min
		if profit > max_profit:
			max_profit = profit
	else:
		min = prices(i)

