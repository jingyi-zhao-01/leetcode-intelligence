# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-beauty-of-the-gardens
# source_path: LeetCode-Solutions-master/Python/maximum-total-beauty-of-the-gardens.py
# solution_class: Solution4
# submission_id: 8c4ef74b446b45077684f623081325f1cc49f0bb
# seed: 3047372057

# Time:  O(nlogn)
# Space: O(1)

import bisect


# sort, prefix sum, greedy, two pointers, improved from solution3

class Solution4(object):
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
            return (prefix[x]-prefix[x-1])*x-prefix[x] <= total

        def binary_search_right(prefix, total, left, right):
            while left <= right:
                mid = left+(right-left)//2
                if not check(prefix, total, mid):
                    right = mid-1
                else:
                    left = mid+1
            return right
    
        flowers.sort()
        n = bisect.bisect_left(flowers, target)
        prefix = [0]*(n+1)
        for i in xrange(n):
            prefix[i+1] = prefix[i]+flowers[i]
        result = suffix = 0
        left = n
        for right in reversed(xrange(n+1)):
            if right != n:
                suffix += flowers[right]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                break
            left = binary_search_right(prefix, total, 1, right)
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result