class Solution(object):
    def countDistinctIntegers(self, nums):
        a = set(nums)
        for i in nums:
            b = int(str(i)[::-1])
            if b not in a:
                a.add(b)
        return len(a)