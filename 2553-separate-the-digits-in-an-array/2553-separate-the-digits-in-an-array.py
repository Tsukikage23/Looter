class Solution(object):
    def separateDigits(self, nums):
        a = list()
        for i in nums:
            for j in str(i):
                a.append(int(j))
        return a