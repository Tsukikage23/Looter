class Solution(object):
    def speed(self,h,piles):
        a = 0
        for i in piles:
            a+=(i+h-1)//h
        return a
    def minEatingSpeed(self, piles, h):
        maxs = max(piles)
        low = 1
        high = maxs
        ans = high
        while low <= high:
            mid = (low+high)//2
            total = self.speed(mid,piles)
            if total <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans