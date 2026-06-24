# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-labels
# source_path: LeetCode-Solutions-master/Python/partition-labels.py
# solution_class: Solution
# submission_id: a85a8b08139084089343e365cce62e5b5f88156c
# seed: 2652342813

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lookup = {c: i for i, c in enumerate(S)}
        first, last = 0, 0
        result = []
        for i, c in enumerate(S):
            last = max(last, lookup[c])
            if i == last:
                result.append(i-first+1)
                first = i+1
        return result