# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: open-the-lock
# source_path: LeetCode-Solutions-master/Python/open-the-lock.py
# solution_class: Solution
# submission_id: 8fb6e85dd347b66cfd7c7d50ae7728541a2d6a7a
# seed: 1373876816

# Time:  O(k * n^k + d), n is the number of alphabets,
#                        k is the length of target,
#                        d is the size of deadends
# Space: O(k * n^k + d)

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead = set(deadends)
        q = ["0000"]
        lookup = {"0000"}
        depth = 0
        while q:
            next_q = []
            for node in q:
                if node == target: return depth
                if node in dead: continue
                for i in xrange(4):
                    n = int(node[i])
                    for d in (-1, 1):
                        nn = (n+d) % 10
                        neighbor = node[:i] + str(nn) + node[i+1:]
                        if neighbor not in lookup:
                            lookup.add(neighbor)
                            next_q.append(neighbor)
            q = next_q
            depth += 1
        return -1