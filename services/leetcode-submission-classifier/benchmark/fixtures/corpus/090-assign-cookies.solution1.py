# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: assign-cookies
# source_path: LeetCode-Solutions-master/Python/assign-cookies.py
# solution_class: Solution
# submission_id: d6915ed60448534bdd3af876ea78c23bed92fbd0
# seed: 1970095760

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        result, i = 0, 0
        for j in xrange(len(s)):
            if i == len(g):
                break
            if s[j] >= g[i]:
                result += 1
                i += 1
        return result