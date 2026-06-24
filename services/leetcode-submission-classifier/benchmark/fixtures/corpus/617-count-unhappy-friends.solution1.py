# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-unhappy-friends
# source_path: LeetCode-Solutions-master/Python/count-unhappy-friends.py
# solution_class: Solution
# submission_id: 5de0743882f7f795ae5acc5f61877a2ed75b090f
# seed: 2520485831

# Time:  O(n^2)
# Space: O(n^2)

class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        friends = [[0]*n for _ in xrange(n)]
        for i in xrange(len(preferences)):
            for j in xrange(len(preferences[i])):
                friends[i][preferences[i][j]] = j
        pairing = [0]*n
        for i, j in pairs:
            pairing[i], pairing[j] = j, i
        return sum(any(friends[i][j] < friends[i][pairing[i]] and friends[j][i] < friends[j][pairing[j]]
                       for j in xrange(len(friends[i])) if j != i and j != pairing[i])
                   for i in xrange(len(friends)))