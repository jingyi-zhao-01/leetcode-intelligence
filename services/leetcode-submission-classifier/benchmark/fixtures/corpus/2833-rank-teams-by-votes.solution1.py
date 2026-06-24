# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rank-teams-by-votes
# source_path: LeetCode-Solutions-master/Python/rank-teams-by-votes.py
# solution_class: Solution
# submission_id: a68322a99bf45d86b723206fc3d6c20cf72c9324
# seed: 3378710809

# Time:  O(m * (n + mlogm)), n is the number of votes
#                          , m is the length of vote
# Space: O(m^2)

class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        count = {v: [0]*len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        return "".join(sorted(votes[0], key=count.__getitem__))