class Solution(object):
    def maximumSubarraySum(self, nums, k):
        left = 0
        window = set()
        maxsum = 0
        sum1 = 0
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                sum1-=nums[left]
                left+=1

            window.add(nums[right])
            sum1 += nums[right]

            if right - left + 1 == k:
                maxsum = max(sum1,maxsum)
                window.remove(nums[left])
                sum1-=nums[left]
                left+=1
            
        return maxsum