# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-taps-to-open-to-water-a-garden
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-taps-to-open-to-water-a-garden.py
# solution_class: Solution
# submission_id: 579897e40e16bdf108925fecb267d37243d0c7e8
# seed: 2042233692

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        def jump_game(A):
            jump_count, reachable, curr_reachable = 0, 0, 0
            for i, length in enumerate(A):
                if i > reachable:
                    return -1
                if i > curr_reachable:
                    curr_reachable = reachable
                    jump_count += 1
                reachable = max(reachable, i+length)
            return jump_count
    
        max_range = [0]*(n+1)
        for i, r in enumerate(ranges):
            left, right = max(i-r, 0), min(i+r, n)
            max_range[left] = max(max_range[left], right-left)
        return jump_game(max_range)