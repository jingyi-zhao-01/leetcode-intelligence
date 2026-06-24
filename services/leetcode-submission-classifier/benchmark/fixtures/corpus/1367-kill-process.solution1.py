# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kill-process
# source_path: LeetCode-Solutions-master/Python/kill-process.py
# solution_class: Solution
# submission_id: 3fb5485912b9ab932606c85b1f7178a892609e65
# seed: 3812382709

# Time:  O(n)
# Space: O(n)

import collections


# DFS solution.

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        def killAll(pid, children, killed):
            killed.append(pid)
            for child in children[pid]:
                killAll(child, children, killed)

        result = []
        children = collections.defaultdict(set)
        for i in xrange(len(pid)):
            children[ppid[i]].add(pid[i])
        killAll(kill, children, result)
        return result