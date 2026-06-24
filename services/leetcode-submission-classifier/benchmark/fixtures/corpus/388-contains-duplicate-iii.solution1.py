# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: contains-duplicate-iii
# source_path: LeetCode-Solutions-master/Python/contains-duplicate-iii.py
# solution_class: Solution
# submission_id: c30bde55432d23eebdfec2f0428da023810c5df3
# seed: 711784767

# Time:  O(n * t)
# Space: O(max(k, t))

import collections

class Solution(object):
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            # Make sure window size
            if len(window) > k:
                window.popitem(False)

            bucket = n if not t else n // t
            # At most 2t items.
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False