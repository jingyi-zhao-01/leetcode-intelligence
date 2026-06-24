# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decompress-run-length-encoded-list
# source_path: LeetCode-Solutions-master/Python/decompress-run-length-encoded-list.py
# solution_class: Solution
# submission_id: 246c15902c59cbeb49d2054649827cd9388900e6
# seed: 577362656

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[i+1] for i in xrange(0, len(nums), 2) for _ in xrange(nums[i])]