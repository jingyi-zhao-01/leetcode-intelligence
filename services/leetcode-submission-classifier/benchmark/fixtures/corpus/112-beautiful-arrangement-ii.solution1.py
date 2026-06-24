# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: beautiful-arrangement-ii
# source_path: LeetCode-Solutions-master/Python/beautiful-arrangement-ii.py
# solution_class: Solution
# submission_id: daa9cb13ac451f91b30ca5608c3d715f5e642e07
# seed: 677366783

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        left, right = 1, n
        while left <= right:
            if k % 2:
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
            if k > 1:
                k -= 1
        return result