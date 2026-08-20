class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        count = 0
        product = 1
        left = 0
        for right in range(len(nums)):
            product*= nums[right]

            while product >= k and left < len(nums)-1:
                product/=nums[left]
                left+=1

            if product < k:
                a = right - left + 1
                count += a

            
        return count