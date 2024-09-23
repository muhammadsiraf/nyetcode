'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = [0,1,1]

Output: []

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
'''
from typing import List

def three_integer_sum(nums: List[int]):
    resolto = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if a > 0:
            break
        
        if i > 0 and a == nums[i-1]:
            continue
        
        l, r = i + 1, len(nums)-1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0 :
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                resolto.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    
    return resolto

listTest = [-1,0,1,2,-1,-4]
result = three_integer_sum(listTest)
print(result)