# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-element-after-replacement-with-digit-sum
# source_path: LeetCode-Solutions-master/Python/minimum-element-after-replacement-with-digit-sum.py
# solution_class: Solution
# submission_id: dbad2ce274f37d834a4a8f4edd72ce168e80185e
# seed: 929423675

# Time:  O(nlogr)
# Space: O(1)

# array

class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result

        return min(f(x) for x in nums)