# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: three-consecutive-odds
# source_path: LeetCode-Solutions-master/Python/three-consecutive-odds.py
# solution_class: Solution
# submission_id: 1ca5def55964cac45334c158f4ca76d535f29de3
# seed: 1360712204

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for x in arr:
            count = count+1 if x%2 else 0
            if count == 3:
                return True
        return False