# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-visited-sector-in-a-circular-track
# source_path: LeetCode-Solutions-master/Python/most-visited-sector-in-a-circular-track.py
# solution_class: Solution
# submission_id: 21f0a3e52cb6b2b3c106802e7e0570e6b2adcf0c
# seed: 2665808115

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        return range(rounds[0], rounds[-1]+1) or \
               range(1, rounds[-1]+1) + range(rounds[0], n+1)