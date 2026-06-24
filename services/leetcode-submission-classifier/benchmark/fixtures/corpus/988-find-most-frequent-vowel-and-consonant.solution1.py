# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-most-frequent-vowel-and-consonant
# source_path: LeetCode-Solutions-master/Python/find-most-frequent-vowel-and-consonant.py
# solution_class: Solution
# submission_id: ab7222dc68ff0c15ce0ffb0260663ce7f58344d6
# seed: 3378510164

# Time:  O(n + 26)
# Space: O(26)

# freq table

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        return max(cnt[i] for i in xrange(26) if chr(i+ord('a')) in VOWELS)+\
               max(cnt[i] for i in xrange(26) if chr(i+ord('a')) not in VOWELS)