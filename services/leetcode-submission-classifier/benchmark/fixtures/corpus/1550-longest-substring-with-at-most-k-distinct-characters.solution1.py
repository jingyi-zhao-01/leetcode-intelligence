# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-with-at-most-k-distinct-characters
# source_path: LeetCode-Solutions-master/Python/longest-substring-with-at-most-k-distinct-characters.py
# solution_class: Solution
# submission_id: a80ab6f97912baf400a97a4b1971ccd05e3c8801
# seed: 630078162

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1
            while distinct_count > k:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1
            longest = max(longest, i - start + 1)
        return longest