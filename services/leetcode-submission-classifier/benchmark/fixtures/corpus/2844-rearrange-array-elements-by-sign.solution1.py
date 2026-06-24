# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-array-elements-by-sign
# source_path: LeetCode-Solutions-master/Python/rearrange-array-elements-by-sign.py
# solution_class: Solution
# submission_id: 71ad28002f1d0ba05bc002009c6f8b55862f5a83
# seed: 3115662993

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos, neg = 0, 1
        result = [0]*len(nums)
        for x in nums:
            if x > 0:
                result[pos] = x
                pos += 2
            else:
                result[neg] = x
                neg += 2
        return result