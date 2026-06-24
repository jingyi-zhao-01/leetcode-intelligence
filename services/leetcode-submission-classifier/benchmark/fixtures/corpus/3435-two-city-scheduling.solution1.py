# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-city-scheduling
# source_path: LeetCode-Solutions-master/Python/two-city-scheduling.py
# solution_class: Solution
# submission_id: 38c984aac65f4de282ffa08181629d027be00b2a
# seed: 767880588

# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(1)

import random


# quick select solution

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        def kthElement(nums, k, compare):
            def PartitionAroundPivot(left, right, pivot_idx, nums, compare):
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in xrange(left, right):
                    if compare(nums[i], nums[right]):
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == k:
                    return
                elif new_pivot_idx > k:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k.
                    left = new_pivot_idx + 1
                    
        kthElement(costs, len(costs)//2, lambda a, b: a[0]-a[1] < b[0]-b[1])
        result = 0
        for i in xrange(len(costs)):
            result += costs[i][0] if i < len(costs)//2 else costs[i][1]
        return result