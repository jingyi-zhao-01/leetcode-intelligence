# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-split-into-subarrays-with-gcd-greater-than-one
# source_path: LeetCode-Solutions-master/Python/minimum-split-into-subarrays-with-gcd-greater-than-one.py
# solution_class: Solution
# submission_id: 99f53a83054ad813abf21952b64fa5f6a049dfe7
# seed: 3246674321

# Time:  O(nlogr), r = max(nums)
# Space: O(1)

# greedy

class Solution(object):
    def minimumSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result, g = 1, 0
        for x in nums:
            g = gcd(g, x)
            if g == 1:
                g = x
                result += 1
        return result