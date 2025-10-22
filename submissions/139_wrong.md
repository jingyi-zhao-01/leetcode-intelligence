# Word Break - Wrong Solution

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        word_set = set(wordDict)
        
        def backtrack(start):
            if start == len(s):
                return True
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    if backtrack(end):
                        return True
            return False
        
        return backtrack(0)