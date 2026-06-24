# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-nice-pairs-in-an-array
# source_path: LeetCode-Solutions-master/Python/count-nice-pairs-in-an-array.py
# solution_class: Solution
# submission_id: 4f9fa99acdfb5f15fcfc6ef52393dfdcd18b1793
# seed: 3371161087

# Time:  O(nlogm), m is max of nums
# Space: O(n)

import collections

class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def rev(x):
            result = 0
            while x:
                x, r = divmod(x, 10)
                result = result*10+r
            return result
        
        result = 0
        lookup = collections.defaultdict(int)
        for num in nums:
            result = (result + lookup[num-rev(num)])%MOD
            lookup[num-rev(num)] += 1
        return result