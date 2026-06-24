# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-incompatibility
# source_path: LeetCode-Solutions-master/Python/minimum-incompatibility.py
# solution_class: Solution
# submission_id: 62fe63c8a79662f6706ab8a8c84991709f9917b7
# seed: 3093853918

# Time:  O(sum(i*d * nCr(i*d, d) * nCr(n, i*d) for i in xrange(1, k+1))) < O(sum(n * 2^m * nCr(n, m) for m in xrange(n+1))) = O(n * 3^n)
# Space: O(n * k)

import itertools

class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        inf = (len(nums)-1)*(len(nums)//k)+1
        def backtracking(nums, d, lookup):
            if not nums:
                return 0
            if nums not in lookup:
                ret = inf
                for new_nums in itertools.combinations(nums, d):
                    new_nums_set = set(new_nums)
                    if len(new_nums_set) < d:
                        continue
                    left = []
                    for num in nums:
                        if num in new_nums_set:
                            new_nums_set.remove(num)
                            continue
                        left.append(num)
                    ret = min(ret, max(new_nums)-min(new_nums) + backtracking(tuple(left), d, lookup))
                lookup[nums] = ret
            return lookup[nums]
        
        result = backtracking(tuple(nums), len(nums)//k, {})
        return result if result != inf else -1