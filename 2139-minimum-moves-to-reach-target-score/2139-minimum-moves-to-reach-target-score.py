class Solution(object):
    def minMoves(self, target, maxDoubles):
        a = 0
        while target != 1:
            if maxDoubles != 0:
                if target % 2 == 0:
                    target//=2
                    maxDoubles-=1
                    a+=1
                    if target == 1:
                        return a
                    elif target % 2 == 1:
                        target-=1
                        a+=1
                        if target == 1:
                            return a
                else:
                    target -= 1
                    a+=1
            else:
                a += target - 1
                target = 1
        return a