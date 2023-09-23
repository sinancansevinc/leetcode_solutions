# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

def mergeAlternately(word1: str, word2: str) -> str:
    merged_string =""
    if len(word1) == len(word2):
        for i in range(0,len(word1)):
            merged_string += word1[i]
            merged_string += word2[i]
            
    else:
        if len(word1) > len(word2):
            for i in range(0,len(word2)):
                merged_string += word1[i]
                merged_string += word2[i]
            
            merged_string+=word1[len(word2):]
            
        else:
            for i in range(0,len(word1)):
                merged_string += word1[i]
                merged_string += word2[i]
            
            merged_string+=word2[len(word1):]
            
            
    
    
    return merged_string
            
word1 = "ab"
word2 = "pqrs"

# print(word2[len(word1):])

print(mergeAlternately(word1,word2))
            
            
    