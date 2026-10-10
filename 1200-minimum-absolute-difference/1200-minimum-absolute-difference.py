class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        a = 10000000
        b = list()
        for i in range(len(arr)-1):
            a = min(a,arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == a:
                b.append([arr[i],arr[i+1]])
        return b