# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-strong-pair-xor-i
# source_path: LeetCode-Solutions-master/Python/maximum-strong-pair-xor-i.py
# solution_class: Solution4
# submission_id: 63f7f4a2b97ec1109527ed8c6a1391564a67e419
# seed: 2593052358

# Time:  O(nlogn + nlogr) = O(nlogr), r = max(nums)
# Space: O(t)

# bit manipulation, greedy, trie, sort, two pointers

class Solution4(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[i]^nums[j] for i in xrange(len(nums)) for j in xrange(i, len(nums)) if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]))