class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        a = []

        def find(ind,target):
            if target == 0:
                ans.append(list(a))
                return
            if ind == len(candidates):
                return
            if candidates[ind] <= target:
                a.append(candidates[ind])
                find(ind,target-candidates[ind])
                a.pop()
            find(ind+1,target)
        find(0,target)
        return ans