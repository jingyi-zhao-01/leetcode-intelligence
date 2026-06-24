# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-substrings-with-distinct-start
# source_path: LeetCode-Solutions-master/Python/maximum-substrings-with-distinct-start.py
# solution_class: Solution2
# submission_id: 2c5c40d6ab095869e00578fc9adfe9681c8f427b
# seed: 3815770523

# Time:  O(n + 26)
# Space: O(26)

# hash table

class Solution2(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        lookup = [False]*26
        for x in s:
            if lookup[ord(x)-ord('a')]:
                continue
            lookup[ord(x)-ord('a')] = True
            result += 1
        return result