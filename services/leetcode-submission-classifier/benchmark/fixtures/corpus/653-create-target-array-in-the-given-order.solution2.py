# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-target-array-in-the-given-order
# source_path: LeetCode-Solutions-master/Python/create-target-array-in-the-given-order.py
# solution_class: Solution2
# submission_id: d181c56eb4f3002995927ac3233e21d43142ac67
# seed: 2341138116

# Time:  O(n^2)
# Space: O(1)

class Solution2(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        result = []
        for i, x in itertools.izip(index, nums):
            result.insert(i, x)
        return result