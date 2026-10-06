class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        l = 2
        r = num//2
        while l <= r:
            mid = (l+r)//2
            a = mid*mid
            if num == a:
                return True
            elif a > num:
                r=mid - 1
            else:
                l = mid+1
        return False