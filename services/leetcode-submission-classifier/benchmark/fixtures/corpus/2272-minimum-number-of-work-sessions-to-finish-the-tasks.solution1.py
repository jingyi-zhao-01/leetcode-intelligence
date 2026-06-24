# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-work-sessions-to-finish-the-tasks
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-work-sessions-to-finish-the-tasks.py
# solution_class: Solution
# submission_id: 3c9273fc4ae956e337e27eaa2fd5d9209b1c728d
# seed: 913029019

# Time:  O(n * 2^n)
# Space: O(2^n)

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        # dp[mask]: min used time by choosing tasks in mask bitset
        dp = [float("inf") for _ in xrange(1<<len(tasks))]
        dp[0] = 0
        for mask in xrange(len(dp)-1):
            basis = 1
            for task in tasks:
                new_mask = mask|basis
                basis <<= 1
                if new_mask == mask:
                    continue
                if dp[mask]%sessionTime + task > sessionTime:
                    task += sessionTime-dp[mask]%sessionTime  # take a break
                dp[new_mask] = min(dp[new_mask], dp[mask]+task)
        return (dp[-1]+sessionTime-1)//sessionTime