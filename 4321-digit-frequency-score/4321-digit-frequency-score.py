class Solution(object):
    def digitFrequencyScore(self, n):
        sum1 = 0
        a = [0]*10
        while n > 0:
            d = n%10
            a[d]+=1
            n//=10
        for i in range(len(a)):
            sum1 += i*a[i]
        return sum1