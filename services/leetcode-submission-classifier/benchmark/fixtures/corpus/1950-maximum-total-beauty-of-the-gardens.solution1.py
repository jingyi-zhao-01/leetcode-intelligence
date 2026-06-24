# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-beauty-of-the-gardens
# source_path: LeetCode-Solutions-master/Python/maximum-total-beauty-of-the-gardens.py
# solution_class: Solution
# submission_id: 297d570cadfe8d9fb61554ecc24af07737418558
# seed: 3675553914

# Time:  O(nlogn)
# Space: O(1)

import bisect


# sort, prefix sum, greedy, two pointers, improved from solution3

class Solution(object):
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
        prefix, suffix = 0, sum(flowers[i] for i in xrange(n))
        result = left = 0
        for right in xrange(n+1):
            if right:
                suffix -= flowers[right-1]
            total = newFlowers-((n-right)*target-suffix)
            if total < 0:
                continue
            while not (left == right or (left and (total+prefix)//left <= flowers[left])):
                prefix += flowers[left]
                left += 1
            mn = min((total+prefix)//left if left else 0, target-1)
            result = max(result, mn*partial+(len(flowers)-right)*full)
        return result