# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-beauty-of-the-gardens
# source_path: LeetCode-Solutions-master/Python/maximum-total-beauty-of-the-gardens.py
# solution_class: Solution3
# submission_id: 298fac60bb02eb3350ec521464807d1da2bc9dcd
# seed: 756265507

# Time:  O(nlogn)
# Space: O(1)

import bisect


# sort, prefix sum, greedy, two pointers, improved from solution3

class Solution3(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
        def check(prefix, total, x):
            return x and (total+prefix[x])//x <= prefix[x+1]-prefix[x]

        def binary_search(prefix, total, left, right):
            while left <= right:
                mid = left+(right-left)//2
                if check(prefix, total, mid):
                    right = mid-1
                else:
                    left = mid+1
            return left
    
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix = [0]*(n+1)
        for i in xrange(n):
            prefix[i+1] = prefix[i]+flowers[i]
        suffix = sum(flowers[i] for i in xrange(n))
        result = left = 0
        for right in xrange(n+1):
            if right:
                suffix -= flowers[right-1]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                continue
            left = binary_search(prefix, total, 0, right-1)
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result