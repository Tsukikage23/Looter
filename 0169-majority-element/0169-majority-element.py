class Solution(object):
    def majorityElement(self, nums):
        a = {}
        maxx = nums[0]
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i]+=1
                if a[maxx] < a[i]:
                    maxx = i
        return maxx