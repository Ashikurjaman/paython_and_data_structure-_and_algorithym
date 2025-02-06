
def buySaleStock(prices):
     n = len(prices)
     if n == 0:
          return 0
     m = prices[0]
     profit = 0

     for i in range(1,n):
          if prices[i] - m:
               profit += prices[i] - m
          m = prices[i]       
     return profit

prices = [7,1,5,3,6,4]

print(buySaleStock(prices))




