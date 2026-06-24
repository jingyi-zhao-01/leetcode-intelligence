# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-valid-pair-of-adjacent-digits-in-string
# source_path: LeetCode-Solutions-master/Python/find-valid-pair-of-adjacent-digits-in-string.py
# solution_class: Solution
# submission_id: fd7db26708a2f63f454d6062a3fda8b010bf5a9f
# seed: 2151626731

# Time:  O(n)
# Space: O(1)

# freq table

class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*9
        for x in s:
            cnt[ord(x)-ord('1')] += 1
        for i in xrange(len(s)-1):
            if s[i] != s[i+1] and cnt[ord(s[i])-ord('1')] == ord(s[i])-ord('0') and cnt[ord(s[i+1])-ord('1')] == ord(s[i+1])-ord('0'):
                return s[i:i+2]
        return ""