class Solution(object):
    def getSneakyNumbers(self, nums):
        a = list()
        b = set()
        for i in nums:
            if i not in b:
                b.add(i)
            else:
                a.append(i)
        return a