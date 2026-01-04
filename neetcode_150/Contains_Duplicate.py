# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

def has_duplicate(nums_list):
    uni_num = set()
    for num in nums_list:
        if num in uni_num:
            return True
        uni_num.add(num)
    
    return False

print(has_duplicate([1, 2, 3, 3]))
print(has_duplicate([1, 2, 3, 4]))