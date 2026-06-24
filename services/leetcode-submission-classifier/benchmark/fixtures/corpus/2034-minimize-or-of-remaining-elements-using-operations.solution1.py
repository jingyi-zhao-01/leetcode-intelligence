# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-or-of-remaining-elements-using-operations
# source_path: LeetCode-Solutions-master/Python/minimize-or-of-remaining-elements-using-operations.py
# solution_class: Solution
# submission_id: 311847e181d7141d1f842383623c657e836f4e3d
# seed: 4274816194

# Time:  O(nlogr)
# Space: O(1)

# bitmasks, greedy

class Solution(object):
    def minOrAfterOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        l = max(nums).bit_length()
        mask = (1<<l)-1
        for i in reversed(xrange(l)):
            result <<= 1
            curr, cnt = mask, 0
            for x in nums:
                curr &= x>>i
                if curr&~result:
                    cnt += 1
                else:
                    curr = mask
            if cnt > k:
                result += 1
        return result