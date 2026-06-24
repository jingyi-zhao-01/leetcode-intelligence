# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-teams
# source_path: LeetCode-Solutions-master/Python/count-number-of-teams.py
# solution_class: Solution
# submission_id: c945f6f0c4c04a70fc4873794a910b9befea95ca
# seed: 3055087478

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(1, len(rating)-1):
            less, greater = [0]*2, [0]*2
            for j in xrange(len(rating)):
                if rating[i] > rating[j]:
                    less[i < j] += 1
                if rating[i] < rating[j]:
                    greater[i < j] += 1
            result += less[0]*greater[1] + greater[0]*less[1]
        return result