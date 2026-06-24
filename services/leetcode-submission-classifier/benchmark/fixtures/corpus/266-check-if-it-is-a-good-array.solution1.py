# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-it-is-a-good-array
# source_path: LeetCode-Solutions-master/Python/check-if-it-is-a-good-array.py
# solution_class: Solution
# submission_id: 38320644e1a15e6b9ff6aa36f3ec097949d39f7a
# seed: 1947005109

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        # Bézout's identity
        result = nums[0]
        for num in nums:
            result = gcd(result, num)
            if result == 1:
                break
        return result == 1