'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1
'''
def change(amount, coins):
    combi = 0
    coins.sort()
    indeks = len(coins)-1
    temp = amount
    while indeks>=0:
        if temp >= coins[indeks]:
            res = temp-coins[indeks]
            if res == 0:
                combi+=1
                indeks-=1
                temp=amount
            else:
                i = indeks
                temp=res            
        else:
            # temp = amount
            indeks-=1
    return combi

testAmount = 5
testCoins = [1,2,5]
result = change(testAmount, testCoins)
print("Result: ", result)