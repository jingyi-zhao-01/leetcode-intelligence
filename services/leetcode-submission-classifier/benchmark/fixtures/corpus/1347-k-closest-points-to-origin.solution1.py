# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-closest-points-to-origin
# source_path: LeetCode-Solutions-master/Python/k-closest-points-to-origin.py
# solution_class: Solution
# submission_id: ef693dc9ba259a2894310705539e425cc0f22ff8
# seed: 1286045358

# Time:  O(n) on average
# Space: O(1)

# quick select solution
from random import randint

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def dist(point):
            return point[0]**2 + point[1]**2
        
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
                pivot_idx = randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == k:
                    return
                elif new_pivot_idx > k:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k.
                    left = new_pivot_idx + 1
                    
        kthElement(points, K-1, lambda a, b: dist(a) < dist(b))
        return points[:K]