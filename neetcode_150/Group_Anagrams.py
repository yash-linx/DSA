# Group Anagrams
# Solved 
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]

# Example 3:
# Input: strs = [""]
# Output: [[""]]

# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

from collections import defaultdict

def group_anagrams(anagram_list):
    res_map = defaultdict(list)
    if len(anagram_list) == 0:
        return [[""]]
    
    for curr_str in anagram_list:
        arr = [0] * 26

        for charac in curr_str:
            arr[ord(charac) - ord('a')] += 1
        
        res_map[tuple(arr)].append(curr_str)

    return list(res_map.values())

print(group_anagrams(["act","pots","tops","cat","stop","hat"]))
print(group_anagrams([""]))