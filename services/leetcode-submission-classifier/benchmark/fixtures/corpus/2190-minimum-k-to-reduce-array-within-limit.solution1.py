# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-k-to-reduce-array-within-limit
# source_path: LeetCode-Solutions-master/Python/minimum-k-to-reduce-array-within-limit.py
# solution_class: Solution
# submission_id: 93295b0e9903efa6a8ba98716863f1fa8c4fd303
# seed: 4209457592

# Time:  O(nlogr + nlogn)
# Space: O(1)

# binary search

class Solution(object):
    def minimumK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(k):
            return sum((ceil_divide(x, k)) for x in nums) <= k**2

        right = max(max(nums), int(ceil(sqrt(len(nums)))))
        return binary_search(1, right, check)