# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ambiguous-coordinates
# source_path: LeetCode-Solutions-master/Python/ambiguous-coordinates.py
# solution_class: Solution
# submission_id: 4e19b53037f043839a90093b9ca8bc2e92c256da
# seed: 2795363658

# Time:  O(n^4)
# Space: O(n)

import itertools

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def make(S, i, n):
            for d in xrange(1, n+1):
                left = S[i:i+d]
                right = S[i+d:i+n]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield "".join([left, '.' if right else '', right])

        return ["({}, {})".format(*cand)
                for i in xrange(1, len(S)-2)
                for cand in itertools.product(make(S, 1, i),
                                              make(S, i+1, len(S)-2-i))]