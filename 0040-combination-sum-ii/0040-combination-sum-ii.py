class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = list()
        ds = list()
        def find(idx,target,ds,ans):
            if target == 0:
                ans.append(list(ds))
                return
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i]) 
                find(i+1,target-candidates[i],ds,ans)
                ds.pop()
        find(0,target,ds,ans)
        return ans