class Solution(object):
    def largestString(self, nums):
        binary = list()
        for i in range(len(nums)):
            a = bin(nums[i])[2:]
            n = len(a)
            j = 0
            s = ""
            while n > 0:
                if a[j] == "1":
                    if n > 26:
                        s+="zz"
                    elif a[j] == "1":
                        s+= chr(n+96)
                n-=1
                j+=1
            binary.append(s)
        return binary