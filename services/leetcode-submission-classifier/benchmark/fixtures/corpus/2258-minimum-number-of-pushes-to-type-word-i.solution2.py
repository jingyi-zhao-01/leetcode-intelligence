# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-pushes-to-type-word-i
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-pushes-to-type-word-i.py
# solution_class: Solution2
# submission_id: 02ad64256816bb809bc3c26da88b79a349941c15
# seed: 427596428

# Time:  O(4)
# Space: O(1)

# greedy

class Solution2(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        return sum(x*(i//(9-2+1)+1) for i, x in enumerate(sorted(collections.Counter(word).itervalues(), reverse=True)))