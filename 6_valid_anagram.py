'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false
'''
def is_anagram(stringA, stringB):
    if len(stringA) != len(stringB):
        return False
    sortedA = sorted(stringA)
    sortedB = sorted(stringB)
    if sortedA == sortedB:
        return True
    else:
        return False
    
stringA = 'kilua'
stringB = 'jam'
test = is_anagram(stringA=stringA, stringB=stringB)
print(test)