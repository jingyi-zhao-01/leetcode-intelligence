# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-distinct-integers-after-reverse-operations
# source_path: LeetCode-Solutions-master/Python/count-number-of-distinct-integers-after-reverse-operations.py
# solution_class: Solution
# submission_id: b1b53c0cde4d18b1714af841d788bc04644526ef
# seed: 1858203708

# Time:  O(nlogr), r = max(nums)
# Space: O(n)

# hash table   

class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(n):
            result = 0
            while n:
                result = result*10 + n%10
                n //= 10
            return result

        return len({y for x in nums for y in (x, reverse(x))})