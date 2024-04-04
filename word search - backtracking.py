def exists(board, word):
    ROWS = len(board)
    COLS = len(board[0])
    
    # to not to visit same path again or same char again
    path = set()
    
    # dfs:- row, col and current char index of word
    def dfs(r, c, i):
        # we have reached at the end of word means we found it
        if i == len(word):
            return True
        
        # out of bounce conditions:
        # indices out of length of board or curr char of word != curr char of board
        # or curr position already in visited path
        if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or 
            word[i] != board[r][c] or 
            (r, c) in path):
            return False

        path.add((r, c))    # found char we want to have, add to path and move to next 
            # look in all adjecent positions
        res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
            
        path.remove((r, c))     # remove recently visited char
        return res
                     
    # now run this dfs on each row and each col of given board
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False    


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word1 = "ABCB"      # False
word2 = "SEE"       # True
word3 = "ABCCED"    # True

print(exists(board, word3))

# TC O((M * N) * 4 * M) -> 4 times running dfs for given length of word 4 * (M) in entire board(M * N)