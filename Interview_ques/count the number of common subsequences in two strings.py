"""                     Count the number of common subsequences in two strings


"""

def count_common_subsequences(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a 2D array to store count of common subsequences
    mat = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column with 0
    for j in range(n + 1):
        mat[0][j] = 0
    for i in range(m + 1):
        mat[i][0] = 0

    # Populate the mat table
    for i in range(m):  # to consider prefixes of s1
        for j in range(n):  # to consider prefixes of s2
            if s1[i] == s2[j]:
                mat[i + 1][j + 1] = mat[i][j] + mat[i][j + 1] + 1
            else:
                mat[i + 1][j + 1] =  mat[i][j + 1] + 1

    # Return the count of common subsequences
    return mat[m][n]


s1 = "ABCD"
s2 = "ACBAD"
print("Number of common subsequences:", count_common_subsequences(s1, s2))
