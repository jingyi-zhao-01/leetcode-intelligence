# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: min-max-game
# source_path: LeetCode-Solutions-master/Python/min-max-game.py
# solution_class: Solution2
# submission_id: 1cc1c3f7afb4a7f197fe4994d8ee2528f5fd140a
# seed: 2510236058

# Time:  O(n)
# Space: O(1)

# simulation, optimized from solution2

class Solution2(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = nums[:]
        while len(q) != 1:
            new_q = []
            for i in xrange(len(q)//2):
                new_q.append(min(q[2*i], q[2*i+1]) if i%2 == 0 else max(q[2*i], q[2*i+1]))
            q = new_q
        return q[0]