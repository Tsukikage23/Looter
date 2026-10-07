class Solution(object):
    def minimumOperations(self, nums):
        a = 0
        for i in nums:
            if i % 3 != 0:
                a += 1
        return a