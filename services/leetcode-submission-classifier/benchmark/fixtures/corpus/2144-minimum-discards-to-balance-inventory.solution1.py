# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-discards-to-balance-inventory
# source_path: LeetCode-Solutions-master/Python/minimum-discards-to-balance-inventory.py
# solution_class: Solution
# submission_id: 6d0683eea03987e8e275fa1268621e93ed607ae5
# seed: 2954373081

# Time:  O(n)
# Space: O(w)

import collections


# freq table, two pointers, sliding window

class Solution(object):
    def minArrivalsToDiscard(self, arrivals, w, m):
        """
        :type arrivals: List[int]
        :type w: int
        :type m: int
        :rtype: int
        """
        result = 0
        cnt = collections.defaultdict(int)
        for i in xrange(len(arrivals)):
            cnt[arrivals[i]] += 1
            if cnt[arrivals[i]] == m+1:
                cnt[arrivals[i]] -= 1
                arrivals[i] = 0
                result += 1
            if i-w+1 >= 0:
                if arrivals[i-w+1]:
                    cnt[arrivals[i-w+1]] -= 1
                    if not cnt[arrivals[i-w+1]]:
                        del cnt[arrivals[i-w+1]]
        return result