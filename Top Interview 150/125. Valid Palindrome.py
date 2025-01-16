
def isPalindrome(s):
    clean_s = re.sub(r'[^a-zA-Z0-9]', '', s)
    if clean_s.lower() == clean_s[::-1].lower():
        return True
    else:
        return False