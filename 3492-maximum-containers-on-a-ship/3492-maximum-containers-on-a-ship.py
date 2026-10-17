class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        a = n*n
        if (maxWeight/w) > a:
            return a
        else:
            return (maxWeight/w)