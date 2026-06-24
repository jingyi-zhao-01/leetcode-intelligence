# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: range-addition-ii
# source_path: LeetCode-Solutions-master/Python/range-addition-ii.py
# solution_class: Solution
# submission_id: 984fab00daad7b2943847a22ceb1a2fc1195b3ec
# seed: 4258384524

# Time:  O(p), p is the number of ops
# Space: O(1)

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        return m*n