# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-operations-to-make-all-elements-divisible-by-three
# source_path: LeetCode-Solutions-master/Python/find-minimum-operations-to-make-all-elements-divisible-by-three.py
# solution_class: Solution2
# submission_id: a38a693a0294a097b9c7d3ad64d38db86b1e8073
# seed: 2523191792

# Time:  O(n)
# Space: O(1)

# math

class Solution2(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(min(x%3, 3-x%3) for x in nums)