# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-frequent-ids
# source_path: LeetCode-Solutions-master/Python/most-frequent-ids.py
# solution_class: Solution2
# submission_id: 8eb84cc781dd276174f71fa773de11bc94fce24f
# seed: 2140042596

# Time:  O(nlogn)
# Space: O(n)

import collections
import itertools
import heapq


# heap

class Solution2(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        result = []
        cnt = collections.Counter()
        cnt2 = collections.Counter()
        sl = SortedList()
        for x, f in itertools.izip(nums, freq):
            sl.discard((cnt[x], cnt2[cnt[x]]))
            cnt2[cnt[x]] -= 1
            if cnt2[cnt[x]]:
                sl.add((cnt[x], cnt2[cnt[x]]))
            cnt[x] += f
            sl.discard((cnt[x], cnt2[cnt[x]]))
            cnt2[cnt[x]] += 1
            sl.add((cnt[x], cnt2[cnt[x]]))
            result.append(sl[-1][0])
        return result