# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-digit-appearances
# source_path: LeetCode-Solutions-master/Python/count-digit-appearances.py
# solution_class: Solution2
# submission_id: 57fa06ebf21c64ddb664a83a42100808ea3bf39b
# seed: 3984619996

# Time:  O(nlogr)
# Space: O(1)

# math

class Solution2(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        return sum(str(x).count(str(digit)) for x in nums)