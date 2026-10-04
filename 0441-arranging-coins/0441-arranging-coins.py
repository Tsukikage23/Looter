class Solution(object):
    def arrangeCoins(self, n):
        i = 1
        j = n
        if n == 1:
            return 1
        while i <= j:
            mid = (i+j)//2
            b = mid*(mid+1)//2
            if b == n:
                return mid
            elif b > n:
                j = mid-1
            elif b < n:
                i = mid+1
        return j