# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        a = 0
        i = 0
        j = n
        while i <= j:
            mid = (i+j)/2
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid) == False:
                i = mid+1
            else:
                j = mid-1
        return 1