# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-digit-appearances
# source_path: LeetCode-Solutions-master/Python/count-digit-appearances.py
# solution_class: Solution
# submission_id: b35a1cb1d4f1d0ae4a767e3f18e1d1c96a71330c
# seed: 1309479939

# Time:  O(nlogr)
# Space: O(1)

# math

class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        def count(x):
            result = 0
            while x:
                x, r = divmod(x, 10)
                if r == digit:
                    result += 1
            return result

        return sum(count(x) for x in nums)