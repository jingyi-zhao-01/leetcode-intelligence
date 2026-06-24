# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-unique-binary-string
# source_path: LeetCode-Solutions-master/Python/find-unique-binary-string.py
# solution_class: Solution2
# submission_id: e030d86dce79b188187982e8aaf1bb01cdf51347
# seed: 2846281951

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        lookup = set(map(lambda x: int(x, 2), nums))  # Time: O(k * n) = O(n^2)
        return next(bin(i)[2:].zfill(len(nums[0])) for i in xrange(2**len(nums[0])) if i not in lookup)  # Time: O(k + n) = O(n)