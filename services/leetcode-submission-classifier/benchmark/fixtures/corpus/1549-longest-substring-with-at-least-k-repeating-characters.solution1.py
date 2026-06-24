# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-with-at-least-k-repeating-characters
# source_path: LeetCode-Solutions-master/Python/longest-substring-with-at-least-k-repeating-characters.py
# solution_class: Solution
# submission_id: 04ef404480de73b6feb850aecda3c6e5ff169253
# seed: 1146032428

# Time:  O(26 * n) = O(n)
# Space: O(26) = O(1)

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def longestSubstringHelper(s, k, start, end):
            count = [0] * 26
            for i in xrange(start, end):
                count[ord(s[i]) - ord('a')] += 1
            max_len = 0
            i = start
            while i < end:
                while i < end and count[ord(s[i]) - ord('a')] < k:
                    i += 1
                j = i
                while j < end and count[ord(s[j]) - ord('a')] >= k:
                    j += 1

                if i == start and j == end:
                    return end - start

                max_len = max(max_len, longestSubstringHelper(s, k, i, j))
                i = j
            return max_len

        return longestSubstringHelper(s, k, 0, len(s))