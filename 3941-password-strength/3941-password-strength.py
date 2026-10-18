class Solution(object):
    def passwordStrength(self, password):
        a = set()
        b = 0
        for i in password:
            if i not in a:
                a.add(i)
                if i in "!@#$":
                    b+=5
                elif i.islower():
                    b+=1
                elif i.isdigit() and 0 <= int(i) <= 9:
                    b+=3
                elif i.isupper():
                    b+=2
        return b