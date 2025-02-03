from typing import List

input = ["neet","code","love","you"]
Output = ["we","say",":","yes"]

def encode(strs: List[str]) -> str:
    stringdecode = ""
    index = 0
    for string in strs:
        stringdecode+=str(len(string))+string
    return stringdecode
        
def decode(s: str) -> List[str]:
    index=0
    arrayOut = []
    while index < len(s):
        panjangString = int(s[index])
        arrayOut.append(s[index:panjangString])
        index+=panjangString
    return arrayOut


    