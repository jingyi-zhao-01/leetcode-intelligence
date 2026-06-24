# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-with-k-frequency-characters-ii
# source_path: LeetCode-Solutions-master/Python/count-substrings-with-k-frequency-characters-ii.py
# solution_class: Solution
# submission_id: 466c824f51690de7bdf90ee9b9b0b0be2a592a5a
# seed: 2925155373

# Time:  O(n + 26)
# Space: O(26)

# freq table, two pointers, sliding window

class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = [0]*26
        result = left = 0
        for right in xrange(len(s)):
            cnt[ord(s[right])-ord('a')] += 1
            while cnt[ord(s[right])-ord('a')] == k:
                result += (len(s)-1)-right+1
                cnt[ord(s[left])-ord('a')] -= 1
                left += 1
        return result