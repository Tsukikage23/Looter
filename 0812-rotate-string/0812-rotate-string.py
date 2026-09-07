class Solution(object):
    def rotateString(self, s, goal):
        a = s*2
        for i in range(len(a)):
            if a[i:i+len(s)] == goal:
                return True
        return False