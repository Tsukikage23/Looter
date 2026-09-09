class Solution(object):
    def findLucky(self, arr):
        a = [0] * 501
        for i in range(len(arr)):
            a[arr[i]] += 1 
        for i in range(len(a) - 1, 0, -1):
            if i == a[i]:
                return i
        return -1