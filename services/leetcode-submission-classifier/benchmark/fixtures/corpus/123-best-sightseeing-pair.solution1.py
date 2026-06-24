# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-sightseeing-pair
# source_path: LeetCode-Solutions-master/Python/best-sightseeing-pair.py
# solution_class: Solution
# submission_id: cc616a1c91748fc881b84b3c161cb468bab98bf9
# seed: 1244802657

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, curr = 0, 0
        for x in A:
            result = max(result, curr+x)
            curr = max(curr, x)-1
        return result