"""
                        Count Vowels, Consonents and Whitespaces

T.C. O(N) - Traversing given sentence
S.C. O(1) - No extra space is used

"""            

def countVandC(s):
    vowels = 0
    consonents = 0
    space = 0
    
    s = s.lower()
    
    for char in s:
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonents += 1
        elif char == " ":
            space += 1
    return f"{vowels}\n{consonents}\n{space}"


s = "Take u forward is Awesome"
print(countVandC(s))
    
