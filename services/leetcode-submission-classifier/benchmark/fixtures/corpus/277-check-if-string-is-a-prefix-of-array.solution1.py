# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-string-is-a-prefix-of-array
# source_path: LeetCode-Solutions-master/Python/check-if-string-is-a-prefix-of-array.py
# solution_class: Solution
# submission_id: 901e41436e5d8afb719e47a269600c5f67890d07
# seed: 3160640713

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        i = j = 0
        for c in s:
            if i == len(words) or words[i][j] != c:
                return False 
            j += 1
            if j == len(words[i]):
                i += 1
                j = 0
        return j == 0