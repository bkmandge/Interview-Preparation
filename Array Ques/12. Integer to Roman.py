"""
12. Integer to Roman (Medium)

eg:- 1500 -> MD, 40 -> XL, 90 -> XC, 400 -> CD, 900 -> CM

Symbol         Value
I               1
V               5
X               10
L               50
C               100
D               500
M               1000

1. create sorted symbol's list -> symList = [sym, value]
2. iterate symbol & value in symbol's list in reversed order -> for sym, val in reversed(symList)
3. check if user given number is divided by value from symbol's list i.e. num > 0 -> num // val
4. again check how many times it can be divided by value, to add symbols in place of numbers -> count = num // val
5.  i.e. sym * count -> res += (sym * count)
6. get remainder for next symbol -> num = num % val
7. return result

"""

def integertoRoman(num: int) -> str:
    symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
               ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
               ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

    res = ""
    for sym, val in reversed(symList):
        if num // val:
            count = num // val
            res += (sym * count)
            num = num % val
    return res


print(integertoRoman(49))
