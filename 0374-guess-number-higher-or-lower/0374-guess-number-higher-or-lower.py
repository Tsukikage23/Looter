# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        i, j = 1, n
        while i<=j:
            mid = (i+j)//2
            a = guess(mid)
            if a == 0:
                return mid
            elif a == 1:
                i = mid+1
            else:
                j = mid-1
        return i