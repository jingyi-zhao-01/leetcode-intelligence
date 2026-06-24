# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-for-cutting-cake-i
# source_path: LeetCode-Solutions-master/Python/minimum-cost-for-cutting-cake-i.py
# solution_class: Solution2
# submission_id: ed0de42a5abb358b0c1c7d4ce9b278ba4fe4794e
# seed: 1195460855

# Time:  O(mlogm + nlogn)
# Space: O(1)

# sort, greedy

class Solution2(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        result = i = j = 0
        while i < len(horizontalCut) or j < len(verticalCut):
            if j == len(verticalCut) or (i < len(horizontalCut) and horizontalCut[i] > verticalCut[j]):
                result += horizontalCut[i]*(j+1)
                i += 1
            else:
                result += verticalCut[j]*(i+1)
                j += 1
        return result