class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        a = 0
        b = 0
        for i in nums1:
            if i in nums2:
                a+=1
        for i in nums2:
            if i in nums1:
                b+=1
        return [a,b]