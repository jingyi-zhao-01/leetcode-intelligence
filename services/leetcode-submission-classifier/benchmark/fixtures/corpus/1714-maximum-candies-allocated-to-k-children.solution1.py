# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-candies-allocated-to-k-children
# source_path: LeetCode-Solutions-master/Python/maximum-candies-allocated-to-k-children.py
# solution_class: Solution
# submission_id: 32bb2a174e8174ba21e52483123c78c54948a5db
# seed: 3429127870

# Time:  O(nlogr), r is max(candies)
# Space: O(1)

# binary search

class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def check(x):
            return sum(c//x for c in candies) >= k

        left, right = 1, max(candies)
        while left <= right:
            mid = left+(right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right