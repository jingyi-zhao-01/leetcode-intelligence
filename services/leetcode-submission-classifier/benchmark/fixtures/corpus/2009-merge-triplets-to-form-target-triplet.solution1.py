# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-triplets-to-form-target-triplet
# source_path: LeetCode-Solutions-master/Python/merge-triplets-to-form-target-triplet.py
# solution_class: Solution
# submission_id: 9804bab4c8c0b6370e6c26fc70739bf98a8fc752
# seed: 2418612823

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        result = [0]*3
        for t in triplets:
            if all(t[i] <= target[i] for i in xrange(3)):
                result = [max(result[i], t[i]) for i in xrange(3)]
        return result == target