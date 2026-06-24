# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-distance-between-unequal-words-in-array-i
# source_path: LeetCode-Solutions-master/Python/maximum-distance-between-unequal-words-in-array-i.py
# solution_class: Solution
# submission_id: f42433b90e628a79352682fbc2b7645c9945d60e
# seed: 1995935493

# Time:  O(n * l)
# Space: O(1)

# array

class Solution(object):
    def maxDistance(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        for i in xrange(len(words)//2+1):
            if words[~i] != words[0] or words[i] != words[-1]:
                return len(words)-i
        return 0