class Solution(object):
    def numIdenticalPairs(self, nums):
        a = [0]*101
        ans = 0
        for i in nums:
            a[i] += 1
        for i in a:
            ans += i*(i-1)/2
        return ans