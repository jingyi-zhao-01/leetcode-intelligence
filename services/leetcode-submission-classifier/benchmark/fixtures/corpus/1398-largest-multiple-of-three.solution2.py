# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-multiple-of-three
# source_path: LeetCode-Solutions-master/Python/largest-multiple-of-three.py
# solution_class: Solution2
# submission_id: c071dc300be52176a4ea095f78a55f3133539fbb
# seed: 617695214

# Time:  O(n)
# Space: O(1)

import collections

class Solution2(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        def candidates_gen(r):
            if r == 0:
                return
            for i in xrange(10):
                yield [i]
            for i in xrange(10):
                for j in xrange(i+1):
                    yield [i, j]

        count, r = collections.Counter(digits), sum(digits)%3
        for deletes in candidates_gen(r):
            delete_count = collections.Counter(deletes)
            if sum(deletes)%3 == r and \
               all(count[k] >= v for k, v in delete_count.iteritems()):
                for k, v in delete_count.iteritems():
                    count[k] -= v
                break
        result = "".join(str(d)*count[d] for d in reversed(xrange(10)))
        return "0" if result and result[0] == '0' else result