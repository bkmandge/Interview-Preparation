
def longestPalindrome(s: str) -> str:
    sLen = len(s)

    res = ""
    longestLen = 0

    for i in range(sLen):
        # check odd length substrings
        # initialise two pointers: left and right
        l = i
        r = i

        # both pointers must in length of a and should have same char to calc palindromic str
        while l >= 0 and r < sLen and s[l] == s[r]:
            if (r - l + 1) > longestLen:
                res = s[l: r + 1]       # store substring in res
                longestLen = r - l + 1  # length of curr substring
            l = l - 1
            r = r + 1
        
        # check even length substrings
        # initialise two pointers: left and right
        l = i
        r = i + 1

        while l >= 0 and r < sLen and s[l] == s[r]:
            if (r - l + 1) > longestLen:
                res = s[l: r + 1]       # store substring in res
                longestLen = r - l + 1  # length of curr substring
            l = l - 1
            r = r + 1
        
    return res


s = "babad"     # bab, aba
s2 = "cbbd"     # bb