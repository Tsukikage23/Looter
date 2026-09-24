class Solution(object):
    def sum2(self,n):
        a = 0
        while n > 0:
            a+=n%10
            n//=10
        return a
    def smallestIndex(self, nums):
        ans = -1
        for i in range(len(nums)):
            sum1 = self.sum2(nums[i])
            if sum1 == i:
                ans = i
                break
        return ans