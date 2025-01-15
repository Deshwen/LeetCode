def lengthOfLastWord(self, s):
    counter = 0
    for i in reversed(s.rstrip()):
        if i != ' ':
            counter = counter + 1
        else:
            break
    return counter 

