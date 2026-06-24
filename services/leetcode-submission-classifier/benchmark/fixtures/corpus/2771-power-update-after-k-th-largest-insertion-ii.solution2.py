# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-update-after-k-th-largest-insertion-ii
# source_path: LeetCode-Solutions-master/Python/power-update-after-k-th-largest-insertion-ii.py
# solution_class: Solution2
# submission_id: 849d20b71b67975eed57e59d766af88a0e9548b8
# seed: 2793594374

# Time:  O((n + q) * log(n * q) + q * logr)
# Space: O(n + q)

from sortedcontainers import SortedList


# sorted list, fast exponentiation

class Solution2(object):
    def powerUpdate(self, nums, p, queries):
        """
        :type nums: List[int]
        :type p: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9+7
        sorted_vals = sorted(set(nums)|set(x[0] for x in queries))
        val_to_idx = {x:i for i, x in enumerate(sorted_vals)}
        bit = BIT(len(val_to_idx))
        for x in nums:
            bit.add(val_to_idx[x], +1)
        result = []
        total = len(nums)
        for x, k in queries:
            bit.add(val_to_idx[x], +1)
            total += 1
            i = bit.kth_element(total-k+1)
            p = pow(p, sorted_vals[i], MOD)
            result.append(p)
        return result