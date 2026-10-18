class Solution(object):
    def buildArray(self, target, n):
        a = 0
        b = list()
        k = max(target)
        while a != k:
            if a+1 in target:
                b.append("Push")
            elif a+1 not in target:
                b.append("Push")
                b.append("Pop")
            a+=1
        
        return b