# using string slicing
def isPalindrome(s):
    rev = s[::-1]
    return s == rev

# checking chars from front-back same time
# s[n-i-1] -> last char
def isPalindrome2(s):
    n = len(s)
    
    for i in range(n):
        if s[i] == s[n-i-1]:
            return True
        else:
            return False

# checking first half only
def isPalindrome3(s):
    n = len(s)
    mid = n // 2
    
    for i in range(mid):
        if s[i] != s[n - i - 1]:
            return False
        else:
            return True
        
        
s = "madam"
print(isPalindrome3(s))
