class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        m = 0 
        for i in a:
            if i-1 not in a:
                l  = 1
                while (i+l) in a:
                    l+=1
                m=max(m,l)
        return m