# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-of-two-numbers-in-an-array
# source_path: LeetCode-Solutions-master/Python/maximum-xor-of-two-numbers-in-an-array.py
# solution_class: Solution2
# submission_id: 0923b26e46254faacefcbbafefe8602f6f41b1e3
# seed: 3380795537

# Time:  O(nlogr), r = max(nums)
# Space: O(t)

class Solution2(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in reversed(xrange(max(nums).bit_length())):
            result <<= 1
            prefixes = set()
            for n in nums:
                prefixes.add(n >> i)
            for p in prefixes:
                if (result | 1) ^ p in prefixes:
                    result |= 1
                    break
        return result