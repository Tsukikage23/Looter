class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        c = 0
        for i in arr1:
            for j in arr2:
                if abs(i-j) <= d:
                    c+=1
                    break
        return len(arr1) - c