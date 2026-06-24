# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-unique-flavors-after-sharing-k-candies
# source_path: LeetCode-Solutions-master/Python/number-of-unique-flavors-after-sharing-k-candies.py
# solution_class: Solution
# submission_id: 78ce57ecee4695e155e3d420ff238dcca2f4c131
# seed: 566744565

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def shareCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter(candies[i] for i in xrange(k, len(candies)))
        result = curr = len(cnt)
        for i in xrange(k, len(candies)):
            cnt[candies[i]] -= 1
            curr += (cnt[candies[i-k]] == 0) - (cnt[candies[i]] == 0)
            cnt[candies[i-k]] += 1
            result = max(result, curr)
        return result