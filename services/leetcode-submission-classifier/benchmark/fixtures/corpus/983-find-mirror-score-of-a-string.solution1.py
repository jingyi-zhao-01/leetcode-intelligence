# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-mirror-score-of-a-string
# source_path: LeetCode-Solutions-master/Python/find-mirror-score-of-a-string.py
# solution_class: Solution
# submission_id: b625404b903259e7b60e7d2f1b453f4392e4da63
# seed: 944256608

# Time:  O(n + 26)
# Space: O(n + 26)

# simulation, hash table, stack

class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        lookup = [[] for _ in xrange(26)]
        for i, x in enumerate(s):
            x = ord(x)-ord('a')
            if lookup[25-x]:
                result += i-lookup[25-x].pop()
            else:
                lookup[x].append(i)
        return result