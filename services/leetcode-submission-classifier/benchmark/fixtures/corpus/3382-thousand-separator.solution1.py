# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: thousand-separator
# source_path: LeetCode-Solutions-master/Python/thousand-separator.py
# solution_class: Solution
# submission_id: 994cefc1e56619c5d30b68e7e7904415790f077a
# seed: 2657549605

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        s = str(n)
        for i, c in enumerate(str(n)):
            if i and (len(s)-i)%3 == 0:
                result.append(".")
            result.append(c)
        return "".join(result)