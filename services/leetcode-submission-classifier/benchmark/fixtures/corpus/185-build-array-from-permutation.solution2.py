# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: build-array-from-permutation
# source_path: LeetCode-Solutions-master/Python/build-array-from-permutation.py
# solution_class: Solution2
# submission_id: 2f017384aececdab26d372fe92da6eafe45a7558
# seed: 1920013133

# Time:  O(n)
# Space: O(1)

# inplace solution

class Solution2(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[x] for x in nums]