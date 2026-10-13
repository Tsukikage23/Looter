class Solution(object):
    def average(self, salary):
        return (sum(salary) - min(salary) - max(salary))/float(len(salary)-2)