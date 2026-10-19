class Solution(object):
    def interpret(self, command):
        a = ""
        b = ""
        for i in range(len(command)):
            if command[i] == "G":
                a += "G"
            elif command[i] == "a":
                a+= "a"
            elif command[i] == "l":
                a += "l"
            elif command[i] == "(" and command[i+1] == ")":
                a+="o"
        return a