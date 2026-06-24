# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-distance-to-type-a-word-using-two-fingers
# source_path: LeetCode-Solutions-master/Python/minimum-distance-to-type-a-word-using-two-fingers.py
# solution_class: Solution
# submission_id: 99eb9f1fcf06ddd8b789665380fd4ae87502fcc0
# seed: 583405005

# Time:  O(26n)
# Space: O(26)

class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def distance(a, b):
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        dp = [0]*26
        for i in xrange(len(word)-1):
            b, c = ord(word[i])-ord('A'), ord(word[i+1])-ord('A')
            dp[b] = max(dp[a] - distance(a, c) + distance(b, c) for a in xrange(26))
        return sum(distance(ord(word[i])-ord('A'), ord(word[i+1])-ord('A')) for i in xrange(len(word)-1)) - max(dp)