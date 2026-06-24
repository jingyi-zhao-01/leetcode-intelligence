# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: arithmetic-subarrays
# source_path: LeetCode-Solutions-master/Python/arithmetic-subarrays.py
# solution_class: Solution
# submission_id: 2c626cb5f99ca051cf85193afd07a39cff6753ee
# seed: 2916423654

# Time:  O(n * q)
# Space: O(n)

import itertools

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def is_arith(n):
            mx, mn, lookup = max(n), min(n), set(n)
            if mx == mn:
                return True
            d, r = divmod(mx-mn, len(n)-1)
            if r:
                return False
            return all(i in lookup for i in xrange(mn, mx, d))
    
        result = []
        for left, right in itertools.izip(l, r):
            result.append(is_arith(nums[left:right+1]))
        return result