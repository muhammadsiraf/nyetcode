'''
Given a string s, return the longest
palindromic
substring
in s.

Example 1:

Input: s = "babab"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 
Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

'''

def check_palindrom_subtring(palindrom):
    longest_ass = [0, 0]
    run = True
    left = 0
    right = len(palindrom)-1
    mid = right/2
    while run:
        print("Left : ", left)
        print("Right : ", right)
        if palindrom[left] != palindrom[right]:
            right -= 1
            mid = right/2
        elif palindrom[left] == palindrom[right]:
            # if right == len(palindrom)-1:
            #     longest_ass = [left, right]
            if right - left > longest_ass[1] - longest_ass[0]:
                longest_ass = [left, right]
            left += 1
            right -= 1
        if palindrom[left] == palindrom[right] and left == right == mid:
            run = False
        if right == 0:
            run = False
            
    if right == 0:
        return None
    
    return palindrom[longest_ass[0]:longest_ass[1]+1]


def check_palindrom_substring_2(palindrom):
    def expand_around_center(left, right):
        print("Enter Here")
        print("Left:", left)
        print("Right:", right)
        while left >= 0 and right < len(palindrom) and palindrom[left] == palindrom[right]:
            print("Left while:", left)
            print("Right while:", right)
            left -= 1
            right += 1
        return left + 1, right - 1

    longest_ass = [0, 0]
    
    for i in range(len(palindrom)):
        # Check for odd length palindromes
        left, right = expand_around_center(i, i)
        if right - left > longest_ass[1] - longest_ass[0]:
            longest_ass = [left, right]
            
        print("Left Legit 1: ", left)
        print("Right Legit 1: ", right)
        
        # Check for even length palindromes
        left, right = expand_around_center(i, i + 1)
        if right - left > longest_ass[1] - longest_ass[0]:
            longest_ass = [left, right]
            
        print("Left Legit: ", left)
        print("Right Legit: ", right)

    if longest_ass[1] - longest_ass[0] == 0:
        return None
    
    return palindrom[longest_ass[0]:longest_ass[1] + 1]


stringTest = 'abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa'
stringTest2 = 'cbbd'
result  = check_palindrom_substring_2(stringTest)
print(result)