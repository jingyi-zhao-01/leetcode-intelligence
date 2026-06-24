# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-numbers-of-function-calls-to-make-target-array
# source_path: LeetCode-Solutions-master/Python/minimum-numbers-of-function-calls-to-make-target-array.py
# solution_class: Solution
# submission_id: 853824138c0d8f4b43d032beb378eaf3d5185287
# seed: 1672757354

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def popcount(n):
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        result, max_len = 0, 1
        for num in nums:
            result += popcount(num)
            max_len = max(max_len, num.bit_length())
        return result + (max_len-1)