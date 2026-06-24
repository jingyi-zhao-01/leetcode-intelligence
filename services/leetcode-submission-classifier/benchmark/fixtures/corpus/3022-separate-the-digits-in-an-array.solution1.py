# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: separate-the-digits-in-an-array
# source_path: LeetCode-Solutions-master/Python/separate-the-digits-in-an-array.py
# solution_class: Solution
# submission_id: b39b51120b0674abf7d79232df1c39038413b047
# seed: 3122021950

# Time:  O(n * logr)
# Space: O(1)

# array

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for x in reversed(nums):
            while x:
                result.append(x%10)
                x //= 10
        result.reverse()
        return result