class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        b = {}
        for char in magazine:
            if char in b:
                b[char] += 1
            else:
                b[char] = 1
        for char in ransomNote:
            if char not in b or b[char] == 0:
                return False
            b[char] -= 1
        return True