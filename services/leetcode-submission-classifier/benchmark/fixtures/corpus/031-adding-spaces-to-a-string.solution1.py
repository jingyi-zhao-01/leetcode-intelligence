# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: adding-spaces-to-a-string
# source_path: LeetCode-Solutions-master/Python/adding-spaces-to-a-string.py
# solution_class: Solution
# submission_id: 8ef6d2376b28467efbb52c72e75bed742b8579d3
# seed: 4207149066

# Time:  O(n)
# Space: O(1)

# inplace solution

class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        prev = len(s)
        s = list(s)
        s.extend([None]*len(spaces))
        for i in reversed(xrange(len(spaces))):
            for j in reversed(xrange(spaces[i], prev)):
                s[j+1+i] = s[j]
            s[spaces[i]+i] = ' '
            prev = spaces[i]
        return "".join(s)