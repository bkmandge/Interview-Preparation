def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    # return ''.join(word1) == ''.join(word2)
    
    word1 = ''.join(word1)
    word2 = ''.join(word2)
    
    return word1 == word2


word1 = ["ab", "c"]; word2 = ["a", "bc"]        # True
word1 = ["a", "cb"]; word2 = ["ab", "c"]        # False
word1  = ["abc", "d", "defg"]; word2 = ["abcddefg"]     # True

