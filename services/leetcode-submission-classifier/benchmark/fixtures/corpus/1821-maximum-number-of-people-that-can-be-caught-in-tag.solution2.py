# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-people-that-can-be-caught-in-tag
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-people-that-can-be-caught-in-tag.py
# solution_class: Solution2
# submission_id: 203fb4db0c85daadc3c78549ccc050afe7541bd6
# seed: 208329344

# Time:  O(n)
# Space: O(1)

# greedy with two pointers solution

class Solution2(object):
    def catchMaximumAmountofPeople(self, team, dist):
        """
        :type team: List[int]
        :type dist: int
        :rtype: int
        """
        result = j = 0
        for i in xrange(len(team)):
            if not team[i]:
                continue
            while j < i-dist:
                j += 1
            while j <= min(i+dist, len(team)-1):
                if team[j] == 0:
                    break
                j += 1
            if j <= min(i+dist, len(team)-1):
                result += 1
                j += 1
        return result