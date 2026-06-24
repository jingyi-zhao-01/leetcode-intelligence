# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-with-lcm-equal-to-k
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-with-lcm-equal-to-k.py
# solution_class: Solution2
# submission_id: c2f066925d1ea0907a641ed60cc5bc007eed13e4
# seed: 2302143688

# Time:  O(n * sqrt(k) * logk)
# Space: O(sqrt(k))

import collections


# dp

class Solution2(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lcm(a, b):
            return a//gcd(a, b)*b

        result = 0
        for i in xrange(len(nums)):
            l = 1
            for j in xrange(i, len(nums)):
                if k%nums[j]:
                    break
                l = lcm(l, nums[j])
                result += int(l == k)
        return result