# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: orderly-queue
# source_path: LeetCode-Solutions-master/Python/orderly-queue.py
# solution_class: Solution
# submission_id: 08398633ffa625c44f4c5e330c2e45a1c754027b
# seed: 1216432031

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            return min(S[i:] + S[:i] for i in xrange(len(S)))
        return "".join(sorted(S))