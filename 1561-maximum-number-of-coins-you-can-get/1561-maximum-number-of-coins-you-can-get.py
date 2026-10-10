class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        a = n/3
        b = 0
        for i in range(n-2,-1,-2):
            if a == 0:
                return b
            b+=piles[i]
            a -= 1
        return b