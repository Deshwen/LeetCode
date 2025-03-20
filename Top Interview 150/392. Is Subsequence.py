def isSubsequence(s, t):
    if len(s) == 0:
        return True
    counter = 0
    for i in t:
        if i == s[counter]:
            counter += 1
            if counter == len(s):
                return True
    return False
