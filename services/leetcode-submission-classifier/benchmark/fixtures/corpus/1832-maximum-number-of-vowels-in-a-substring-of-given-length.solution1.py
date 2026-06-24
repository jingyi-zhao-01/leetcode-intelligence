# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-vowels-in-a-substring-of-given-length
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-vowels-in-a-substring-of-given-length.py
# solution_class: Solution
# submission_id: f3291c2d56282a69ce0de0a97052f741dc77306e
# seed: 1019446905

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        VOWELS = set("aeiou")
        result = curr = 0
        for i, c in enumerate(s):
            curr += c in VOWELS
            if i >= k:
                curr -= s[i-k] in VOWELS
            result = max(result, curr)
        return result