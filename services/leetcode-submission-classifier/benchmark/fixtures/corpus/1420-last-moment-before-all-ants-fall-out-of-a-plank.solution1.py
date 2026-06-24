# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-moment-before-all-ants-fall-out-of-a-plank
# source_path: LeetCode-Solutions-master/Python/last-moment-before-all-ants-fall-out-of-a-plank.py
# solution_class: Solution
# submission_id: ca59e06e7a7fa6975b317d23b4f9ef99c1d90b86
# seed: 854167302

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        return max(max(left or [0]), n-min(right or [n]))