# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n) time without using the division operation?

# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

# Example 2:
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

def productExceptSelf(nums: list[int]) -> list[int]:
    # post_fix = [0] * len(nums)
    # pre_fix = [0] * len(nums)

    # prefix_product, postfix_product = 1, 1
    # j = len(nums)-1
    # for i in range(len(nums)):
    #     pre_fix[i] = prefix_product
    #     post_fix[j] = postfix_product
    #     prefix_product *= nums[i]
    #     postfix_product *= nums[j]
    #     j-=1
    # return [pre_fix[i]*post_fix[i] for i in range(len(pre_fix))]

    result = [0] * len(nums)
    prefix_product, postfix_product = 1, 1
    for i in range(len(nums)):
        result[i] = prefix_product
        prefix_product *= nums[i]

    for j in range(len(nums)-1, -1, -1):
        result[j] = result[j]*postfix_product
        postfix_product *= nums[j]

    return result
    

print(productExceptSelf([-1,0,1,2,3]))

