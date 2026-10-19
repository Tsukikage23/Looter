class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        a = 0
        for i in hours:
            if i >= target:
                a+=1
        return a