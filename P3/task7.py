def ispalindrome(s: str):
    # range(len(s)) = 0, 1, 2, ... , len(s) - 1
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

s = input()

print(ispalindrome(s))