# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-robots-within-budget
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-robots-within-budget.py
# solution_class: Solution
# submission_id: 86599c15ce311dc21ef34cd5e464aa8161de870f
# seed: 2094641440

# Time:  O(n)
# Space: O(n)

import collections


# sliding window, two pointers, mono deque

class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        result = left = curr = 0
        dq = collections.deque()
        for right in xrange(len(chargeTimes)):
            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)
            curr += runningCosts[right]
            if chargeTimes[dq[0]]+(right-left+1)*curr > budget:
                if dq[0] == left:
                    dq.popleft()
                curr -= runningCosts[left]
                left += 1
        return right-left+1