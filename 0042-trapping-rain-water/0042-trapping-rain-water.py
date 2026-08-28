class Solution(object):
    def trap(self, height):
        l = 1
        r = len(height)-2
        lmax = height[l-1]
        rmax = height[r+1]
        water = 0
        while l<=r:
            lmax = max(lmax,height[l])
            rmax = max(rmax,height[r])
            if lmax < rmax:
                water+= lmax - height[l]
                l+=1
            else:
                water+=rmax-height[r]
                r-=1
        return water