'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

Explanation: "tabacat" is not a palindrome.

Constraints:

    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.

'''
def is_palindrome(s:str):
    s = s.lower()
    s = s.replace(' ', '')
    chars_to_remove = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    s = ''.join(c for c in s if c not in chars_to_remove)
    pertama = s[0:len(s)//2]
    kedua = s[:len(s)//2-1:-1]
    if len(s)%2 == 1:
        pertama = s[0:len(s)//2]
        kedua = s[:len(s)//2:-1]
        
    print(len(s))
    print(pertama)
    print(kedua)
    if pertama == kedua:
        return True
    else:
        return False
    # # if []
    # return s

stringTest = "No lemon, no melon"
print(is_palindrome(stringTest))