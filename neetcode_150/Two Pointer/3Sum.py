# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        while i>0 and nums[i-1]==nums[i]:
            i += 1
        j = i + 1
        k = len(nums)-1
        while(j < k):
            summy = nums[i] + nums[j] + nums[k]
            if summy == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while(nums[j-1]==nums[j]):
                    j+=1
                while(nums[k+1]==nums[k]):
                    k -= 1
            elif summy < 0:
                j+=1
                
            else:
                k -= 1
            
    return result

print(threeSum([-1,0,1,2,-1,-4]))