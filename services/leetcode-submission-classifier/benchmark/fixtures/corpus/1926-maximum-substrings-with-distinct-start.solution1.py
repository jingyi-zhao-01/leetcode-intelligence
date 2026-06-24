# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-substrings-with-distinct-start
# source_path: LeetCode-Solutions-master/Python/maximum-substrings-with-distinct-start.py
# solution_class: Solution
# submission_id: 912de6accc7233086790eed23cdfde0d9d5a5a2a
# seed: 2434286998

# Time:  O(n + 26)
# Space: O(26)

# hash table

class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))