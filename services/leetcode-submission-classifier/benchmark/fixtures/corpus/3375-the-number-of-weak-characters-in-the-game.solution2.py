# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-weak-characters-in-the-game
# source_path: LeetCode-Solutions-master/Python/the-number-of-weak-characters-in-the-game.py
# solution_class: Solution
# submission_id: 1d448b2fcd33787cfbcf270e3575c77706144716
# seed: 1730156395

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        lookup = collections.defaultdict(list)
        for a, d in properties:
            lookup[a].append(d)
        result = max_d = 0
        for a in sorted(lookup.iterkeys(), reverse=True):
            result += sum(d < max_d for d in lookup[a])
            max_d = max(max_d, max(lookup[a]))
        return result