class Solution(object):
    def findDifferentBinaryString(self, nums):
        a = ""
        for i in range(len(nums)):
            if nums[i][i] == "0":
                a+="1"
            else:
                a+="0"
        return a