# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-gcd-of-formed-pairs
# source_path: LeetCode-Solutions-master/Python/sum-of-gcd-of-formed-pairs.py
# solution_class: Solution
# submission_id: 343becd70ede47a4dbaa625a2b3c7e2042009dc3
# seed: 3913116009

# Time:  O(nlogr)
# Space: O(n)

# prefix sum, sort, two pointers

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        mx = 0
        prefix = []
        for x in nums:
            mx = max(mx, x)
            prefix.append(gcd(mx, x))
        prefix.sort()
        result = 0
        left, right = 0, len(nums)-1
        while left < right:
            result += gcd(prefix[left], prefix[right])
            left += 1
            right -= 1
        return result