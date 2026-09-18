class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count = 0
        sum1=0
        a = sum(costs)
        if costs[0] > coins:
            return count
        if a <= coins:
            return len(costs)
        for i in costs:
            sum1+=i
            count+=1
            if sum1 == coins:
                return count
            elif sum1 >= coins:
                count-=1
                break
        return count