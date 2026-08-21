class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        n = len(nums)
        ans = [-1]*n
        for i in range(2*len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if stack:
                ans[i%n] = stack[-1]
            stack.append(nums[i%n])
        return ans
        