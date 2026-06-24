# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-additions-to-make-valid-string
# source_path: LeetCode-Solutions-master/Python/minimum-additions-to-make-valid-string.py
# solution_class: Solution
# submission_id: a9345e049a14fc1868e0ceb14bf18f631edea248
# seed: 1639468596

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        return 3*(sum(i-1 < 0 or word[i-1] >= word[i] for i in xrange(len(word))))-len(word)