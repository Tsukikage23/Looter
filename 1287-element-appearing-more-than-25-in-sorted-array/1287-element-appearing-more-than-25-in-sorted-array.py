class Solution(object):
    def findSpecialInteger(self, arr):
        a = len(arr)/4
        b = arr[0]
        c = 0
        for i in range(len(arr)):
            if arr[i] == b:
                c+=1
                if c > a:
                    return b
            elif arr[i] !=b:
                b = arr[i]
                c = 1
        return 1