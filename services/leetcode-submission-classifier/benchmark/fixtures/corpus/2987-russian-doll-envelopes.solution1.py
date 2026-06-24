# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: russian-doll-envelopes
# source_path: LeetCode-Solutions-master/Python/russian-doll-envelopes.py
# solution_class: Solution
# submission_id: 14d34dea837054301a3607c3fc4a477bde0756ec
# seed: 1451187947

# Time:  O(nlogn + nlogk) = O(nlogn), k is the length of the result.
# Space: O(1)

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def insert(target):
            left, right = 0, len(result) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if result[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(result):
                result.append(target)
            else:
                result[left] = target

        result = []

        envelopes.sort(lambda x, y: y[1] - x[1] if x[0] == y[0] else \
                                    x[0] - y[0])
        for envelope in envelopes:
            insert(envelope[1])

        return len(result)