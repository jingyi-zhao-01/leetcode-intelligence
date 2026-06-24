# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intervals-between-identical-elements
# source_path: LeetCode-Solutions-master/Python/intervals-between-identical-elements.py
# solution_class: Solution
# submission_id: 2eeb8be9e833a49b367555a548f230932db74c09
# seed: 588214007

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        lookup = collections.defaultdict(list)
        for i, x in enumerate(arr):
            lookup[x].append(i)
        result = [0]*len(arr)
        for idxs in lookup.itervalues():
            prefix = [0]
            for i in idxs:
                prefix.append(prefix[-1]+i)
            for i, idx in enumerate(idxs):
                result[idx] = (idx*(i+1)-prefix[i+1]) + ((prefix[len(idxs)]-prefix[i])-idx*(len(idxs)-i))
        return result