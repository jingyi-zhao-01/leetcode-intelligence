# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-substring-with-two-occurrences
# source_path: LeetCode-Solutions-master/Python/maximum-length-substring-with-two-occurrences.py
# solution_class: Solution2
# submission_id: 19b654e10cdae18f1064f9eee0365850577e5a7b
# seed: 3378710780

# Time:  O(n + 26)
# Space: O(26)

# freq table, sliding window, two pointers

class Solution2(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        COUNT = 2
        result = 0
        cnt = [0]*26
        left = 0
        for right, x in enumerate(s):
            cnt[ord(x)-ord('a')] += 1
            while cnt[ord(x)-ord('a')] > COUNT:
                cnt[ord(s[left])-ord('a')] -= 1
                left += 1
            result = max(result, right-left+1)
        return result