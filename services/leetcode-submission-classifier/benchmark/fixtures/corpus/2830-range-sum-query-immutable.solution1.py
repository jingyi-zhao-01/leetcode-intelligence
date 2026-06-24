# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: range-sum-query-immutable
# source_path: LeetCode-Solutions-master/Python/range-sum-query-immutable.py
# solution_class: Solution
# submission_id: 45868ea8b67b50b2635849598a4bc3d4817a9407
# seed: 1084230728

# Time:  ctor:   O(n),
#        lookup: O(1)
# Space: O(n)

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu.append(self.accu[-1] + num),

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]



