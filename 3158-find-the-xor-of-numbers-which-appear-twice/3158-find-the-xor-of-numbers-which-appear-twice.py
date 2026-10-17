class Solution(object):
    def duplicateNumbersXOR(self, nums):
        a = set()
        b = 0
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                b ^= i
        return b