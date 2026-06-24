# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-multiple-of-three
# source_path: LeetCode-Solutions-master/Python/largest-multiple-of-three.py
# solution_class: Solution
# submission_id: 985e1c0d0da0abbb2fc6ff50ccb1baba549c7a19
# seed: 1326541231

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        lookup = {0: [],
                  1: [(1,), (4,), (7,), (2, 2), (5, 2), (5, 5), (8, 2), (8, 5), (8, 8)],
                  2: [(2,), (5,), (8,), (1, 1), (4, 1), (4, 4), (7, 1), (7, 4), (7, 7)]}
        count = collections.Counter(digits)
        for deletes in lookup[sum(digits)%3]:
            delete_count = collections.Counter(deletes)
            if all(count[k] >= v for k, v in delete_count.iteritems()):
                for k, v in delete_count.iteritems():
                    count[k] -= v
                break
        result = "".join(str(d)*count[d] for d in reversed(xrange(10)))
        return "0" if result and result[0] == '0' else result