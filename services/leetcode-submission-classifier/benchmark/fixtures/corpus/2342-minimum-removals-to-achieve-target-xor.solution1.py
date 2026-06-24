# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-removals-to-achieve-target-xor
# source_path: LeetCode-Solutions-master/Python/minimum-removals-to-achieve-target-xor.py
# solution_class: Solution
# submission_id: 1ebe23712098acac47c4cc8afd7a7cf90d6388bf
# seed: 2517022134

# Time:  O(n * r), r = max(nums)
# Space: O(r)

# bitmasks, bfs

class Solution(object):
    def minRemovals(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bfs():
            dist = {}
            dist[0] = 0
            q = [0]
            while q:
                new_q = []
                for k in q:
                    if k == target:
                        return dist[k]
                    for x in nums:
                        if k^x in dist:
                            continue
                        dist[k^x] = dist[k]+1
                        new_q.append(k^x)
                q = new_q
            return -1

        target ^= reduce(lambda accu, x: accu^x, nums, 0)
        return bfs()