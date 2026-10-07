class Solution(object):
    def recoverOrder(self, order, friends):
        a = list()
        for i in order:
            if i in friends:
                a.append(i)
        return a