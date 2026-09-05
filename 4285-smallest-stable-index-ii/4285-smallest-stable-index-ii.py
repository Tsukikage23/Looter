class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        prefixmax = [0]*n
        suffixmin = [0]*n
        prefixmax[0] = nums[0]
        suffixmin[-1] = nums[-1]
        ans = 99999
        for i in range(1,n):
            prefixmax[i] = max(prefixmax[i-1],nums[i])
            suffixmin[n-i-1] = min(suffixmin[n-i],nums[n-1-i])
        for i in range(n):
            score = prefixmax[i] - suffixmin[i]
            if score<=k:
                ans = min(ans,i)
        if ans == 99999:
            return -1
        return ans