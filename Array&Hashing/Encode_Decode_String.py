'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res =""
        for string in strs:
            res+=str(len(string))+"#"+string
        return res
        

    def decode(self, s: str) -> List[str]:
        res =[]
        i=0
        while i < len(s):
            j=i+1
            while s[j] != '#':
                j+=1
            size = int(s[i:j])
            i=j+1
            res.append(s[i:i+size])
            i = i+size
        return res