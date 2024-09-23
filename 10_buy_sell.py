def maxProfit(prices):
    max = 0
    for i, a in enumerate(prices):
        j = len(prices)-1
        while j > i:
            print("a: ", a)
            print("b:", prices[j])
            if prices[j]-a >= max:
                max = prices[j] - a
            j-=1
            
    return max

testPrices = [10,1,5,6,7,1]
result = maxProfit(testPrices)
print("Result : ", result)