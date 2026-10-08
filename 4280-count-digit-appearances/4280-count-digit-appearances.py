class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        c = 0
        for i in range(len(nums)):
            while str(digit) in str(nums[i]):
                nums[i] = str(nums[i]).replace(str(digit),"",1)
                c += 1
        return c