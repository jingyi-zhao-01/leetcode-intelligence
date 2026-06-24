# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-largest-group
# source_path: LeetCode-Solutions-master/Python/count-largest-group.py
# solution_class: Solution
# submission_id: 2c409252dd68f1c7ed3502a7b3917811453e1af1
# seed: 1738508452

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = collections.Counter()
        for x in xrange(1, n+1):
            count[sum(map(int, str(x)))] += 1
        max_count = max(count.itervalues())
        return sum(v == max_count for v in count.itervalues())