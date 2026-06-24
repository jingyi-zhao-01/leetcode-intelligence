# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: array-partition-i
# source_path: LeetCode-Solutions-master/Python/array-partition-i.py
# solution_class: Solution
# submission_id: 77f18367a4dd91291fbc225d5e40924c5d2d3f22
# seed: 3393145039

# Time:  O(r), r is the range size of the integers
# Space: O(r)

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LEFT, RIGHT = -10000, 10000
        lookup = [0] * (RIGHT-LEFT+1)
        for num in nums:
            lookup[num-LEFT] += 1
        r, result = 0, 0
        for i in xrange(LEFT, RIGHT+1):
            result += (lookup[i-LEFT] + 1 - r) / 2 * i
            r = (lookup[i-LEFT] + r) % 2
        return result