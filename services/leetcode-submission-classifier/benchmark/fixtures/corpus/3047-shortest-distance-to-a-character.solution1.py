# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-distance-to-a-character
# source_path: LeetCode-Solutions-master/Python/shortest-distance-to-a-character.py
# solution_class: Solution
# submission_id: d1eaf8edce8bb1ecd9b8f0f0b5de486de83c32c4
# seed: 351877488

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = [len(S)] * len(S)
        prev = -len(S)
        for i in itertools.chain(xrange(len(S)),
                                 reversed(xrange(len(S)))):
            if S[i] == C:
                prev = i
            result[i] = min(result[i], abs(i-prev))
        return result