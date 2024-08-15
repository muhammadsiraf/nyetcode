'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''
from typing import List
def groupAnagram(strs: List[str]) -> List[List[str]]:
    hash_anagram = {}
    kepet = []
    for item in strs:
        str_sorted = sorted(item)
        string_yeni = ''.join(str_sorted)
        if hash_anagram.get(string_yeni):
            array_temp = hash_anagram[string_yeni]
            array_temp.append(item)
            hash_anagram[string_yeni] = array_temp
        else:
            hash_anagram[string_yeni] = [item]

    for keys in hash_anagram:
        kepet.append(hash_anagram[keys])
    
    return kepet

strs = ["act","pots","tops","cat","stop","hat"]

result = groupAnagram(strs)
print("Resulto: ", result)