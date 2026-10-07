class Solution(object):
    def differenceOfSums(self, n, m):
        ans = 0
        for i in range(n+1):
            if i%m != 0:
                ans+=i
            else:
                ans-=i
        return ans