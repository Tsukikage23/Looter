class Solution(object):
    def isGood(self, nums):
        n = max(nums)
        a = set()
        b = 0
        if len(nums) != n+1:
            return False
        for i in nums:
            if i not in a:
                a.add(i)
            elif i in a:
                if i != n:
                    return False
                b += 1
        if b != 1:
            return False
        return True