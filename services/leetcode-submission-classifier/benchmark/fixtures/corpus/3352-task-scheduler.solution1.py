# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: task-scheduler
# source_path: LeetCode-Solutions-master/Python/task-scheduler.py
# solution_class: Solution
# submission_id: 1c5e16c1acb33844aa5a35d5a0d61c3bdfe8cf27
# seed: 2512222411

# Time:  O(n)
# Space: O(26) = O(1)

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        _, max_count = counter.most_common(1)[0]
        return max((max_count-1) * (n+1) + counter.values().count(max_count), len(tasks))