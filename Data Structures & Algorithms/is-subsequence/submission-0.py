class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ponitr in t:
            if i < len(s) and s[i] == ponitr:
                i+=1
        return i == len(s)