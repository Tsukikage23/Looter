class Solution(object):
    def reorderSpaces(self, text):
        a = 0
        b = ""
        c = list()
        for i in text:
            if i == " ":
                a+=1
                if b:
                    c.append(b)
                    b = ""
            else:
                b+=i
        if b:
            c.append(b)
        if len(c) == 1:
            return c[0] + " "*a
        d = a/(len(c)-1)
        e = a - (d*(len(c)-1))
        f = ""
        for i in range(len(c)):
            f+=c[i]
            if i!=len(c)-1:
                f+= " "*d
        f+= " "*e
        return f