# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-difference-between-two-pairs
# source_path: LeetCode-Solutions-master/Python/maximum-product-difference-between-two-pairs.py
# solution_class: Solution
# submission_id: 9625f84dd3300676b1a991a2fd88ee2ce1a54416
# seed: 2456189360

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, smallest = [0]*2, [float("inf")]*2
        for x in nums:
            if x >= largest[0]:
                largest[:] = [x, largest[0]]
            elif x > largest[1]:
                largest[1] =x
            if x <= smallest[0]:
                smallest[:] = [x, smallest[0]]
            elif x < smallest[1]:
                smallest[1] = x
        return largest[0]*largest[1] - smallest[0]*smallest[1]