# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]
from collections import defaultdict
def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq_map = {}
    for i in nums:
        freq_map[i] = freq_map.get(i, 0) + 1

    freq_list = [[] for i in range(len(nums)+1)]
    for key, value in freq_map.items():

        freq_list[value].append(key)
    print(freq_list)
    print(freq_map)
    ans_list = []
    for j in range(len(freq_list)-1, -1, -1):
        if(len(freq_list[j])==0):
            continue
        for num in freq_list[j]:
            if not k<=0:
                ans_list.append(num)
                k -= 1
            else: 
                return ans_list

print(topKFrequent([1,2,2,3,3,3,3, 6,6,6,6], 3))