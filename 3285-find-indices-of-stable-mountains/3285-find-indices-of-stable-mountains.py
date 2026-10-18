class Solution(object):
    def stableMountains(self, height, threshold):
        a = list()
        for i in range(1,len(height)):
            if height[i-1] >  threshold:
                a.append(i)
        return a