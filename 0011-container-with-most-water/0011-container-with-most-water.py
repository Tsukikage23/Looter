class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        pani = 0
        while i <= j:
            a = min(height[i],height[j])
            pani = max(pani,a*(j-i))
            if a == height[i]:
                i+=1
            if a == height[j]:
                j-=1
        return pani