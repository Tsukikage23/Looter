class Solution(object):
    def heightChecker(self, heights):
        a = sorted(heights)
        count = 0
        for i in range(len(a)):
            if a[i] != heights[i]:
                count+=1
        return count