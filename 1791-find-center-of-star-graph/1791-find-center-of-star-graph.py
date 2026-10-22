class Solution(object):
    def findCenter(self, edges):
        a = edges[0][0]
        b = edges[0][1]
        for i in edges:
            if a not in i:
                a = 0
            if b not in i:
                b = 0
        if a!= 0:
            return a
        else:
            return b