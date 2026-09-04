class Solution(object):
    def maxProduct(self, nums):
        pre = 1
        suf = 1
        ans = -10
        n = len(nums)
        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre*=nums[i]
            suf*=nums[n-1-i]
            ans = max(ans,(max(pre,suf)))
        return ans