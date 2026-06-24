# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-revert-word-to-initial-state-i
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-revert-word-to-initial-state-i.py
# solution_class: Solution2
# submission_id: a3af4a80d085ca68b1c0fdc4803fa385a32b3b23
# seed: 79941941

# Time:  O(n)
# Space: O(n)

# z-function

class Solution2(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        for i in xrange(k, len(word), k):
            if all(word[i+j] == word[j] for j in xrange(len(word)-i)):
                return i//k
        return ceil_divide(len(word), k)