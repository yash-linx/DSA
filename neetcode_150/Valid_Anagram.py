# Valid Anagram
# Solved 
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_count = [0] * 26

    for i in range(len(str1)):
        char_count[ord(str1[i])- ord('a')] += 1
        char_count[ord(str2[i])- ord('a')] -= 1

    for val in char_count:
        if val != 0:
            return False
     
    return True

s = "racecar"
t = "carrace"
print(is_anagram(s,t))