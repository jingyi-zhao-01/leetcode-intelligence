# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-with-gcd-equal-to-k
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-with-gcd-equal-to-k.py
# solution_class: Solution2
# submission_id: d10553830f5d90d899bf34b9a1417199a6e87559
# seed: 2233255540

# Time:  O(nlogr), r = max(nums)
# Space: O(logr)

# dp

class Solution2(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result = 0
        for i in xrange(len(nums)):
            g = 0
            for j in xrange(i, len(nums)):
                if nums[j]%k:
                    break
                g = gcd(g, nums[j])
                result += int(g == k)
        return result