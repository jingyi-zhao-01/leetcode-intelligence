# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-smallest-number-from-di-string
# source_path: LeetCode-Solutions-master/Python/construct-smallest-number-from-di-string.py
# solution_class: Solution
# submission_id: ad58a6c4efbd4d3f5a5d971b5892754d37799548
# seed: 1008396200

# Time:  O(n)
# Space: O(1)

# constructive algorithms

class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        result = []
        for i in xrange(len(pattern)+1):
            if not (i == len(pattern) or pattern[i] == 'I'):
                continue
            for x in reversed(range(len(result)+1, (i+1)+1)):
                result.append(x)
        return "".join(map(str, result))