# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stable-subarrays-with-equal-boundary-and-interior-sum
# source_path: LeetCode-Solutions-master/Python/stable-subarrays-with-equal-boundary-and-interior-sum.py
# solution_class: Solution2
# submission_id: 455cc970d92ae612b7226aebe22a2267e3273eac
# seed: 2858116692

# Time:  O(n)
# Space: O(n)

import collections


# freq table, prefix sum

class Solution2(object):
    def countStableSubarrays(self, capacity):
        """
        :type capacity: List[int]
        :rtype: int
        """
        cnt = collections.defaultdict(lambda: collections.defaultdict(int))
        result = prefix = 0
        for i, x in enumerate(capacity):
            result += cnt[x][prefix-x]
            prefix += x
            cnt[x][prefix] += 1
            if x == 0 and i-1 >= 0 and capacity[i-1] == 0:
                result -= 1
        return result