class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tuple1 = tuple(nums)
        tuple1 *= 2
        return list(tuple1)