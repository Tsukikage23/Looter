class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        for i in range(n//2-1,-1,-1):
            self.heapify(nums,n,i)
        for i in range(n-1,0,-1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums,i,0)
        return nums
    def heapify(self,nums,n,i):
        largest = i
        l = 2*i+1
        r = 2*i+2
        if l<n and nums[l]>nums[largest]:
            largest = l
        if r<n and nums[r]>nums[largest]:
            largest = r
        if largest !=i:
            nums[i],nums[largest] = nums[largest],nums[i]
            self.heapify(nums,n,largest)        