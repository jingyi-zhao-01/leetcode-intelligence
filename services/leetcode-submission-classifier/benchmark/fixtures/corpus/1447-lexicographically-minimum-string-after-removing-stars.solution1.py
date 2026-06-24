# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-minimum-string-after-removing-stars
# source_path: LeetCode-Solutions-master/Python/lexicographically-minimum-string-after-removing-stars.py
# solution_class: Solution
# submission_id: e3d7498e8f834f84d6f1af5e616dba72c7cdde93
# seed: 3155821238

# Time:  O(n + 26)
# Space: O(n + 26)

# greedy, hash table, stack

class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        lookup = [[] for _ in range(26)]
        for i, x in enumerate(s):
            if x != '*':
                lookup[ord(x)-ord('a')].append(i)
                continue
            for stk in lookup:
                if not stk:
                    continue
                result[stk.pop()] = '*'
                break
        return "".join(x for x in result if x != '*')