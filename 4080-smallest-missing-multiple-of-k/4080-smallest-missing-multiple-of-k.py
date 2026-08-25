class Solution(object):
    def missingMultiple(self, nums, k):
        i = k
        while True:
            if i not in nums:
                return i
            i += k
        