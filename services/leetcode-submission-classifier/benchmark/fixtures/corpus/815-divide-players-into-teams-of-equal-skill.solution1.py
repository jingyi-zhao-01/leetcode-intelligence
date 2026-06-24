# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-players-into-teams-of-equal-skill
# source_path: LeetCode-Solutions-master/Python/divide-players-into-teams-of-equal-skill.py
# solution_class: Solution
# submission_id: e23056cdf7024d1aba54183dd47504972edf40bf
# seed: 2338358592

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """

        target = sum(skill)//(len(skill)//2)
        cnt = collections.Counter(skill)
        result = 0
        for k, v in cnt.iteritems():
            if target-k not in cnt or cnt[target-k] != cnt[k]:
                return -1
            result += k*(target-k)*v
        return result//2