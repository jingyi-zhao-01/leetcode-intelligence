# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-have-distinct-elements
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-have-distinct-elements.py
# solution_class: Solution
# submission_id: 1b37bccde6d0aca42847cdf805dcf618e0f7729b
# seed: 2896436275

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 3
        def ceil_divide(a, b):
            return (a+b-1)//b

        lookup = set()
        while nums:
            if nums[-1] in lookup:
                break
            lookup.add(nums.pop())
        return ceil_divide(len(nums), L)