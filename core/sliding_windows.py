'''
Given an array of integers and a number k, 
find the maximum sum of any contiguous subarray of size k.
'''
def max_sum_subarray(arr,k):
    n = len(arr)
    if n < k:
        return None
    
    max_sum = sum(arr[:k])
    current_max = max_sum

    for i in range(k, n):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)

    return max_sum


'''
Given an array of integers, 
find the length of the smallest contiguous subarray 
whose sum is greater than or equal to a given value s.
'''
def var_len_sliding(array_input, value_s):
    pointer_left = 0
    pointer_right = 0
    max_sum = sum(array_input[0:1])
    
    while max_sum != value_s and pointer_right+1 < len(array_input):
        print("Pointer Left: ", pointer_left)
        print("Pointer Right: ", pointer_right)
        max_sum = sum(array_input[pointer_left:pointer_right+1])
        print("Maks: ", max_sum)
        if max_sum > value_s:
            pointer_left += 1
        elif max_sum < value_s:
            pointer_right += 1
        
            
        print("Resulto: {} indeces {};{} length {}".format(max_sum, pointer_left, pointer_right, pointer_right-pointer_left+1))
            
    
    return [max_sum, pointer_right - pointer_left + 1]

'''
sliding windows test
'''
# array_yeni = [110,4,90,34,8,89]
# array_worst = [0,0,0,0,0,0,0,0]
# result = var_len_sliding(array_worst, 132)
# print('result: ', result)


'''
Longest Substring Without Repeating Characters
'''
def longest_substring(string):
    substring = ''
    point_left = 0
    point_right = 0
    max = 0
    indeces_max = "{};{}".format(point_left, point_right)
    hash = {}
    
    while point_right < len(string):
        if (string[point_right] in hash and hash[string[point_right]] >= point_left):
            print("Masok Hash ", string[point_right])
            point_left = hash[string[point_right]] + 1

        if (point_right-point_left+1 >= max):
                max = point_right-point_left+1
                indeces_max = "{};{}".format(point_left, point_right)

        hash[string[point_right]] = point_right
        print("Hash: ", hash)
        point_right += 1
        print("Resulto: ", [max, indeces_max])
        
                
    return [max, indeces_max]

# def lengthOfLongestSubstring(s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         pointer_left = 0
#         pointer_right = 0
#         longest_len = 0
#         char_kepet = {}
#         for char in s:
            
#             if char in char_kepet and char_kepet[char] > pointer_left:
#                 pointer_left = char_kepet[char]+1
                
#             if longest_len < pointer_right - pointer_left + 1:
#                 longest_len = pointer_right - pointer_left + 1

#             char_kepet[char] = pointer_right
#             pointer_right+=1

#         return longest_len

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    pointer_left = 0
    longest_len = 0
    char_kepet = {}
    
    for pointer_right in range(len(s)):
        char = s[pointer_right]
        
        if char in char_kepet and char_kepet[char] >= pointer_left:
            pointer_left = char_kepet[char] + 1
            
        longest_len = max(longest_len, pointer_right - pointer_left + 1)

        char_kepet[char] = pointer_right

    return longest_len
            
    
string_long = "bhdgjsadoieqekjqwkhaszxc"
result = longest_substring(string_long)
print("RESULTO FINAL String: ", result)

'''
Smallest Subarray with a Given Sum
Input: arr = [2, 1, 5, 2, 3, 2], S = 7
Output: 2
'''
def smallest_subarray_sum(array, s):
    pointer_left = 0
    pointer_right = 0
    current_sum = 0
    min_length = len(array)+1
    combi = "{}.{}".format(0,0)  
    
    while pointer_right+1 < len(array):
        current_sum += array[pointer_right]
        
        while current_sum >= s:
            print("Masuk situ")
            if pointer_right - pointer_left != 0:
                if pointer_right - pointer_left + 1 < min_length:
                    min_length=pointer_right-pointer_left+1
                    combi="{}.{}".format(pointer_left, pointer_right)
            
            current_sum -= array[pointer_left]
            pointer_left+=1
            
        pointer_right+=1
        print("Current Sum: ", current_sum)
        
    # for pointer_right in range(len(array)):
    
    if min_length == len(array) + 1:
        return 0, combi
    else:
        return min_length, combi

# def smallest_subarray_sum(array, s):
#     pointer_left = 0
#     current_sum = 0
#     min_length = len(array) + 1
#     combi = "0.0"  
    
#     for pointer_right in range(len(array)):
#         current_sum += array[pointer_right]

#         # While the current sum is greater than or equal to s, try to shrink the window
#         while current_sum >= s:
#             # Check if the current window size is the smallest found so far
#             if pointer_right - pointer_left + 1 < min_length:
#                 min_length = pointer_right - pointer_left + 1
#                 combi = "{}.{}".format(pointer_left, pointer_right)
            
#             # Shrink the window by moving the left pointer to the right
#             current_sum -= array[pointer_left]
#             pointer_left += 1

#         print("Current Sum: ", current_sum)
        
#     # If no valid subarray was found, return 0 or appropriate value
#     if min_length == len(array) + 1:
#         return 0, combi
#     else:
#         return min_length, combi

# array_yeni = [2, 1, 5, 2, 3, 2]
# s = 7
# resulto = smallest_subarray_sum(array_yeni, s)
# print("Resulto: ", resulto)

'''
Dynamic Average Questions
Simple Dynamic Average:

    Question: Implement a data structure that supports the following operations:
        addNum(int num): Adds an integer num to the data stream.
        getAverage(): Returns the average of all elements in the current data stream.
    Follow-up: Optimize the space and time complexity of your implementation.
'''

class newDataStructure():
    def __init__(self):
        self.coreData = []
    
    def addNum(self, number):
        self.coreData.append(number)
        
    def getAverage(self):
        avg = sum(self.coreData[:len(self.coreData)])/len(self.coreData)
        return avg
    
# brekeleData = newDataStructure()
# brekeleData.addNum(1)
# brekeleData.addNum(4)
# brekeleData.addNum(5)
# brekeleData.addNum(3)
# brekeleData.addNum(4)
# brekeleData.addNum(5)
# brekeleData.addNum(6)
# averageResult = brekeleData.getAverage()
# print("Average: ", averageResult)
