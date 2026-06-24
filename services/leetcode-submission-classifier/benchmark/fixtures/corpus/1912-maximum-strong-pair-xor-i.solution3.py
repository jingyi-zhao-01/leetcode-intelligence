# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-strong-pair-xor-i
# source_path: LeetCode-Solutions-master/Python/maximum-strong-pair-xor-i.py
# solution_class: Solution3
# submission_id: 70470c7a9a33185b3871b856b381459833f5183c
# seed: 48828850

# Time:  O(nlogn + nlogr) = O(nlogr), r = max(nums)
# Space: O(t)

# bit manipulation, greedy, trie, sort, two pointers

class Solution3(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in reversed(xrange(max(nums).bit_length())):
            prefix_min, prefix_max = {}, {}
            for x in nums:
                y = x>>i
                if y not in prefix_min:
                    prefix_min[y] = prefix_max[y] = x
                prefix_min[y] = min(prefix_min[y], x)
                prefix_max[y] = max(prefix_max[y], x)
            result <<= 1
            for x in prefix_min.iterkeys():
                y = (result|1)^x
                assert(x != y)
                if y in prefix_max and prefix_min[max(x, y)] <= 2*prefix_max[min(x, y)]:
                    result |= 1
                    break
        return result