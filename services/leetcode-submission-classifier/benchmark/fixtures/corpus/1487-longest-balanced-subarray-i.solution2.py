# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-balanced-subarray-i
# source_path: LeetCode-Solutions-master/Python/longest-balanced-subarray-i.py
# solution_class: Solution2
# submission_id: ddf47070fc075d402e569b6e70a8e9fffccffd6c
# seed: 90404077

# Time:  O(nlogn)
# Space: O(n)

# segment tree, binary search, prefix sum

class Solution2(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for left in xrange(len(nums)):
            curr = 0
            lookup = set()
            for right in xrange(left, len(nums)):
                if nums[right] not in lookup:
                    lookup.add(nums[right])
                    curr += 1 if nums[right]&1 else -1
                if curr == 0:
                    result = max(result, right-left+1)
        return result