# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-substring-with-two-occurrences
# source_path: LeetCode-Solutions-master/Python/maximum-length-substring-with-two-occurrences.py
# solution_class: Solution
# submission_id: 9b87894630d6e80ace90b2000060e8f69407d63a
# seed: 2704432822

# Time:  O(n + 26)
# Space: O(26)

# freq table, sliding window, two pointers

class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        COUNT = 2
        result = 0
        cnt = [0]*26
        left = invalid_cnt = 0
        for right, x in enumerate(s):
            if cnt[ord(x)-ord('a')] == COUNT:
                invalid_cnt += 1
            cnt[ord(x)-ord('a')] += 1
            if invalid_cnt:
                cnt[ord(s[left])-ord('a')] -= 1
                if cnt[ord(s[left])-ord('a')] == COUNT:
                    invalid_cnt -= 1
                left += 1
        return right-left+1