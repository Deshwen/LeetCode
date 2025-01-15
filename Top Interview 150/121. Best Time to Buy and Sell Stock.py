
def maxProfit(prices):
        lowest = 0
        highest = 1
        maxProfit = 0
        while highest < len(prices):
            if prices[lowest] < prices[highest]:
                profit = prices[highest] - prices[lowest]
                maxProfit = max(maxProfit, profit)
            else:
                lowest = highest
            highest = highest + 1
        return maxProfit

maxProfit([7,1,5,3,6,4])

