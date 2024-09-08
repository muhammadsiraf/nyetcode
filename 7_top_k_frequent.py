'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.

'''
def k_most_frequent(arrayNumber, k):
    hash = {}

    for i in arrayNumber:
        if i in hash:
            value = hash[i]
            hash[i] = value + 1
        else:
            hash[i] = 1
    
    listArray = list(dict(sorted(hash.items(), key=lambda item: item[1], reverse=True)))
    
    return listArray[0:k]


arrayTest = [1,2,2,4,4,4]
k = 2
result = k_most_frequent(arrayTest, 2)
print(result)