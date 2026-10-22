class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        a = [0]*n
        j = 0
        k = 1
        for i in nums:
            if i > 0:
                a[j] = i
                j+=2
            else:
                a[k] = i
                k+=2
        return a