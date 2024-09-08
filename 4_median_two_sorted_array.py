'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
'''
def median_two_sorted_array(nums1, nums2):
    merged_array = []
    merged_length = len(nums1) + len(nums2)
    median_index = merged_length // 2
    print("Median index : ", median_index)
    array_one_pointer = 0
    array_two_pointer = 0
    while len(merged_array) < median_index+1:
        if array_one_pointer < len(nums1) and array_two_pointer < len(nums2):
            if nums1[array_one_pointer] <= nums2[array_two_pointer]:
                merged_array.append(nums1[array_one_pointer])
                array_one_pointer+=1
            elif nums2[array_two_pointer] < nums1[array_one_pointer]:
                merged_array.append(nums2[array_two_pointer])
                array_two_pointer+=1
        elif array_one_pointer < len(nums1):
            merged_array.append(nums1[array_one_pointer])
            array_one_pointer+=1
        elif array_two_pointer < len(nums2):
            merged_array.append(nums2[array_two_pointer])
            array_two_pointer+=1
    
    if merged_length % 2 == 0:
        return (merged_array[median_index] + merged_array[median_index-1]) / 2
    else:
        return (merged_array[median_index])
            
    
array_yeni1 = [1,2]
array_yeni2 = []
result = median_two_sorted_array(array_yeni1, array_yeni2)
print("Result : ", result)