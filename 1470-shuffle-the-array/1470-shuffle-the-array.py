class Solution(object):
    def shuffle(self, nums, n):
        i = 0
        j = n
        a = list()
        while j != n*2:
            a.append(nums[i])
            a.append(nums[j])
            i+=1
            j+=1
        return a