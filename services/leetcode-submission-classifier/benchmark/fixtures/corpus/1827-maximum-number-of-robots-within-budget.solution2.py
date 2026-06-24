# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-robots-within-budget
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-robots-within-budget.py
# solution_class: Solution2
# submission_id: 2bafaa6881708278db34baea2325498b9b64866b
# seed: 3947606852

# Time:  O(n)
# Space: O(n)

import collections


# sliding window, two pointers, mono deque

class Solution2(object):
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
            while dq and chargeTimes[dq[0]]+(right-left+1)*curr > budget:
                if dq[0] == left:
                    dq.popleft()
                curr -= runningCosts[left]
                left += 1
            result = max(result, right-left+1)            
        return result