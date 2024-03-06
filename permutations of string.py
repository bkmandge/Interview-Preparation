"""                         Permutations of string
A permutation also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered list S
into a one-to-one correspondence with S itself.

A string of length N has N! permutations.

S = “ABC”
Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”

"""


def toString(List):
    return ''.join(List)

# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.


def permute(a, l, r):
    if r == l:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]

            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


string = "ABC"
n = len(string)
a = list(string)

permute(a, 0, n)
