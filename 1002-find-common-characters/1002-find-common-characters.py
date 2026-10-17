class Solution(object):
    def commonChars(self, words):
        a = list(words[0])
        for i in range(1,len(words)):
            b = list()
            c = words[i]
            for j in a:
                if j in c:
                    c = c.replace(j,"",1)
                    b.append(j)
            a = b
        return a