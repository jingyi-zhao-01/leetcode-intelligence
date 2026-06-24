# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-operations-with-the-same-score-ii
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-operations-with-the-same-score-ii.py
# solution_class: Solution
# submission_id: 357a58d6acc5f1c2b64729868e0248b5f23486dd
# seed: 3995686721

# Time:  O(n^2)
# Space: O(n^2)

# memoization

class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def memoization(left, right, target, lookup):
            if not right-left+1 >= 2:
                return 0
            if lookup[left][right] == -1:
                lookup[left][right] = max(1+memoization(left+2, right-0, target, lookup) if nums[left]+nums[left+1]   == target else 0,
                                          1+memoization(left+1, right-1, target, lookup) if nums[left]+nums[right]    == target else 0,
                                          1+memoization(left+0, right-2, target, lookup) if nums[right-1]+nums[right] == target else 0)
            return lookup[left][right] 

        return max(memoization(0, len(nums)-1, target, [[-1]*(len(nums)) for _ in xrange(len(nums))]) for target in {nums[0]+nums[1], nums[0]+nums[-1], nums[-2]+nums[-1]})