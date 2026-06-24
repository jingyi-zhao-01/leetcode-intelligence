# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-popular-video-creator
# source_path: LeetCode-Solutions-master/Python/most-popular-video-creator.py
# solution_class: Solution
# submission_id: 595194d29f4e9a11345e98c18017eb8cba31e6c6
# seed: 1543817788

# Time:  O(n)
# Space: O(n)

import collections
import itertools


# hash table

class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        cnt = collections.Counter()
        lookup = collections.defaultdict(lambda: (float("inf"), float("inf")))
        for c, i, v in itertools.izip(creators, ids, views):
            cnt[c] += v
            lookup[c] = min(lookup[c], (-v, i))
        mx = max(cnt.itervalues())
        return [[k, lookup[k][1]] for k, v in cnt.iteritems() if v == mx]