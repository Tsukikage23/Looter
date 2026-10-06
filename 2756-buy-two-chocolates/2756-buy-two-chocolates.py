class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        for i in range(len(prices)-1):
            sum1 = prices[i]+prices[i+1]
            if sum1 <= money:
                money -= sum1
            return money
            
        return 1