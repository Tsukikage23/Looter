class Solution(object):
    def maximumWealth(self, accounts):
        a = 0
        for i in range(len(accounts)):
            a = max(a,sum(accounts[i]))
        return a