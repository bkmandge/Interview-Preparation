"""
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

s = "s"  -> "s"

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2,
both will result "leEeetcode" to be reduced to "leetcode".

"""


def makeGood(s: str) -> str:
    stack = []
    n = len(s)
    i = 0
    while i < n:
        # to remove if chars are equal check below conditions
        # stack should not be empty
        # curr char of s should not be equal to stack's top element
        # lower case letters of both chars

        if (stack and
            stack[-1] != s[i] and
            stack[-1].lower() == s[i].lower()
            ):
            stack.pop() # remove prev char from stack
        else:
            stack.append(s[i])
        i = i + 1

    return "".join(stack)


s = "abBAcC"
s2 = "leEeetcode"

print(makeGood(s2))
