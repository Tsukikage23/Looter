class Solution(object):
    def findClosestNumber(self, nums):
        s = 1000000
        ans = 0
        for i in nums:
            c = abs(i-0)
            if s > c:
                s = c
                ans = i
            elif s == c:
                if i < 0 and ans < 0:
                    ans = i
                else:
                    ans = abs(ans)
        return ans