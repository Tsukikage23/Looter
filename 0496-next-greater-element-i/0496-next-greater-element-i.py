class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        ans = []
        dit = dict()
        for i in range(len(nums2)-1 ,-1,-1):
            while(len(stack) != 0 and stack[-1] <= nums2[i]):
                stack.pop()
            if len(stack) == 0:
                dit[nums2[i]] = -1
            else:
                dit[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            ans.append(dit[nums1[i]])
        return ans