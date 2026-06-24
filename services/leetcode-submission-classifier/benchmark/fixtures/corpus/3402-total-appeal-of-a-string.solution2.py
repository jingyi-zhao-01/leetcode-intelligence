# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-appeal-of-a-string
# source_path: LeetCode-Solutions-master/Python/total-appeal-of-a-string.py
# solution_class: Solution2
# submission_id: 5b64c04381a7828f93407e548e75c29ba19efce8
# seed: 1195511067

# Time:  O(n)
# Space: O(26)

# combinatorics

class Solution2(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = cnt = 0
        lookup = [-1]*26
        for i, c in enumerate(s):
            cnt += i-lookup[ord(c)-ord('a')]
            lookup[ord(c)-ord('a')] = i
            result += cnt
        return result