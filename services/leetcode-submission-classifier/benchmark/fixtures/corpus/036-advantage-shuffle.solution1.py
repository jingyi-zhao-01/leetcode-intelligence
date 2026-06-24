# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: advantage-shuffle
# source_path: LeetCode-Solutions-master/Python/advantage-shuffle.py
# solution_class: Solution
# submission_id: b66e16deef56d6458cd26e58cc0228737a4e7244
# seed: 752688964

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)

        candidates = {b: [] for b in B}
        others = []
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                candidates[sortedB[j]].append(a)
                j += 1
            else:
                others.append(a)
        return [candidates[b].pop() if candidates[b] else others.pop()
                for b in B]