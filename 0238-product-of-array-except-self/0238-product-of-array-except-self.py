class Solution(object):
    def productExceptSelf(self, nums):
        a = list()
        b = [1]*len(nums)
        a.append(nums[0])
        b[-1] = nums[-1]
        for i in range(1,len(nums)):
            a.append(nums[i]*a[i-1])
        for j in range(len(nums)-2,-1,-1):
            b[j] = b[j+1] * nums[j]
        c = [1]*len(nums)
        c[0] = b[1]
        c[-1] = a[-2]
        for i in range(1,len(nums)-1):
            c[i] = a[i-1] * b[i+1]
        return c