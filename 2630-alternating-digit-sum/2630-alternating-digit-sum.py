class Solution(object):
    def alternateDigitSum(self, n):
        a = str(n)
        sum1 =0
        sum2 = 0
        for i in range(len(a)):
            if i%2==0:
                sum1 += int(a[i])
            else:
                sum2+=int(a[i])
        return sum1 - sum2