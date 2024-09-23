'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

'''
def merge_sort_array(nums1, m, nums2, n):
    # result = []
    # i = 0
    # j = 0
    # if n == 0:
    #     return nums2
    # elif m == 0:
    #     return nums1
    
    # while i < m or j < n:
        
    #     if i >= m and j < n:
    #         result.append(nums2[j])
    #         j+=1
    #     if j >= n and i < m:
    #         result.append(nums1[i])
    #         i+=1
        
    #     if (i<m and j <n):
    #         if nums1[i] >= nums2[j] and (i<m and j <n):
    #             result.append(nums2[j])
    #             j+=1
    #         else:
    #             result.append(nums1[i])
    #             i+=1
    i = m - 1
    j = n - 1
    k = m+n-1
    
    while j >= 0:
        if i > 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            
        k -= 1
            
    return nums1

testArray1 = [1,2,3,0,0,0]
testArray2 = [2,5,6]
n = 3
m = 3
result = merge_sort_array(testArray1, n, testArray2, m)
print(result)