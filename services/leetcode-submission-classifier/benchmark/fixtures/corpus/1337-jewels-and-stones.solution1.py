# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jewels-and-stones
# source_path: LeetCode-Solutions-master/Python/jewels-and-stones.py
# solution_class: Solution
# submission_id: 82d126744b0585ee1cf1e2463d02c01cf880eb78
# seed: 1802384213

# Time:  O(m + n)
# Space: O(n)

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        lookup = set(J)
        return sum(s in lookup for s in S)