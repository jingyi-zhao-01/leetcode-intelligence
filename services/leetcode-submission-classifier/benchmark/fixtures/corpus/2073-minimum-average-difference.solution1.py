# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-average-difference
# source_path: LeetCode-Solutions-master/Python/minimum-average-difference.py
# solution_class: Solution
# submission_id: 51e7ebfcc723f987bffd25d4cf1390521ee5b9fb
# seed: 282360114

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        mn, idx = float("inf"), -1
        prefix = 0
        for i, x in enumerate(nums):
            prefix += x
            a = prefix//(i+1)
            b = (total-prefix)//(len(nums)-(i+1)) if i+1 < len(nums) else 0
            diff = abs(a-b)
            if diff < mn:
                mn, idx = diff, i
        return idx