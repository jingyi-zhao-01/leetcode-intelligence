# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-beauty-of-the-gardens
# source_path: LeetCode-Solutions-master/Python/maximum-total-beauty-of-the-gardens.py
# solution_class: Solution2
# submission_id: f64c0dec1a504227bd5b464e2650d9a024e5ae12
# seed: 2245976591

# Time:  O(nlogn)
# Space: O(1)

import bisect


# sort, prefix sum, greedy, two pointers, improved from solution3

class Solution2(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
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
                continue
            left = min(left, right)
            while not (left == 0 or (prefix[left]-prefix[left-1])*left-prefix[left] <= total):
                left -= 1
            mn = min((total+prefix[left])//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result