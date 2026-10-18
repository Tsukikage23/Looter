f = [0,1,1]
while len(f) < 50:
    f.append(f[-1]+f[-2])
class Solution(object):
    def threeFibonacciSum(self, n):
        for i in range(2,len(f)):
            if f[i-2]+f[i-1] + f[i] == n:
                return True
        return False