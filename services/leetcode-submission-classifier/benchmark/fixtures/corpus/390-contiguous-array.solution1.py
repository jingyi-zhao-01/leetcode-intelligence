# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: contiguous-array
# source_path: LeetCode-Solutions-master/Python/contiguous-array.py
# solution_class: Solution
# submission_id: 4abc92086bc903edb41133c617f82e6a2af08330
# seed: 2828957389

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0, 0
        lookup = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in lookup:
                result = max(result, i - lookup[count])
            else:
                lookup[count] = i

        return result