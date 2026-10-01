class Solution(object):
    def replaceElements(self, arr):
        max1 = -1
        n = len(arr)
        ans = [-1]*n
        if n == 0:
            return arr
        for i in range(n-1,-1,-1):
            if i == n-1:
                ans[i] = -1
                max1 = max(max1,arr[i])
            else:
                ans[i] = max1
                max1 = max(max1,arr[i])
        return ans