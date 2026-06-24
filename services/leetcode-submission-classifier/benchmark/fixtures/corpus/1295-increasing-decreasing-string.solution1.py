# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: increasing-decreasing-string
# source_path: LeetCode-Solutions-master/Python/increasing-decreasing-string.py
# solution_class: Solution
# submission_id: 501720262de4f7d7f51a104c5a12681e9e09d661
# seed: 98803281

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result, count = [], [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1
        while len(result) != len(s):
            for c in xrange(len(count)):
                if not count[c]:
                    continue
                result.append(chr(ord('a')+c))
                count[c] -= 1
            for c in reversed(xrange(len(count))):
                if not count[c]:
                    continue
                result.append(chr(ord('a')+c))
                count[c] -= 1
        return "".join(result)