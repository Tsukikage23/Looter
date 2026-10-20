class Solution(object):
    def countKDifference(self, nums, k):
        a = 0
        for i in nums:
            for j in nums:
                if i!=j:
                    if i - j == k:
                        a+=1
        return a