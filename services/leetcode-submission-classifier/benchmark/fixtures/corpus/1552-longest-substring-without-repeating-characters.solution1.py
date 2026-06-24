# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-without-repeating-characters
# source_path: LeetCode-Solutions-master/Python/longest-substring-without-repeating-characters.py
# solution_class: Solution
# submission_id: 2997dbf0d983598e740af7e7be3d29e0a821c383
# seed: 3960283892

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, left = 0, 0
        lookup = {}
        for right in xrange(len(s)):
            if s[right] in lookup:
                left = max(left, lookup[s[right]]+1)
            lookup[s[right]] = right
            result = max(result, right-left+1)
        return result