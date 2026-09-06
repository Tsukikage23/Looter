class Solution(object):
    def countRotations(self, s, k):
        ans = 0
        n = len(s)
        for i in range(n):
            score = 0
            for j in range(i,n+i-1):
                if s[j%n] == s[(j+1)%n]:
                    score+=1
            if score == k:
                ans+=1
        return ans