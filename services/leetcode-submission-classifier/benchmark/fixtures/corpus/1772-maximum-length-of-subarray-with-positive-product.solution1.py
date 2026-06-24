# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-subarray-with-positive-product
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-subarray-with-positive-product.py
# solution_class: Solution
# submission_id: 9b6188fc3ae7e0e116ca007a943aa97a14b799cd
# seed: 3890783573

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, neg_cnt, last_zero_pos, first_valid_neg_pos = 0, 0, -1, -1
        for i in xrange(len(nums)):
            if nums[i] == 0:
                neg_cnt = 0
                last_zero_pos = i
                first_valid_neg_pos = -1
                continue
            if nums[i] < 0:
                if first_valid_neg_pos == -1:
                    first_valid_neg_pos = i
                neg_cnt += 1
            result = max(result, i-(last_zero_pos if neg_cnt%2 == 0 else first_valid_neg_pos))
        return result