# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 4sum
# source_path: LeetCode-Solutions-master/Python/4sum.py
# solution_class: Solution3
# submission_id: 7b8aff57f38e29482ccf78e7ded368d110090315
# seed: 2947643180

# Time:  O(n^3)
# Space: O(1)

import collections


# Two pointer solution. (1356ms)

class Solution3(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                lookup[nums[i] + nums[j]].append([i, j])

        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and \
                           b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)