# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rank-transform-of-an-array
# source_path: LeetCode-Solutions-master/Python/rank-transform-of-an-array.py
# solution_class: Solution
# submission_id: 33692ad809632c717684365d4611abcc297a7fd2
# seed: 2613345653

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return map({x: i+1 for i, x in enumerate(sorted(set(arr)))}.get, arr)