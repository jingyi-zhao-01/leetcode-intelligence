# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-array-can-be-sorted
# source_path: LeetCode-Solutions-master/Python/find-if-array-can-be-sorted.py
# solution_class: Solution2
# submission_id: db190a3fdd7e7a64db23cd0e8d355970e611f8ce
# seed: 2155371500

# Time:  O(n)
# Space: O(1)

# sort

class Solution2(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def popcount(x):
            return bin(x).count("1")
        
        def pairwise(it):
            a, b = tee(it)
            next(b, None)
            return itertools.izip(a, b)

        return all(max(a) <= min(b) for a, b in pairwise(list(it) for key, it in groupby(nums, popcount)))