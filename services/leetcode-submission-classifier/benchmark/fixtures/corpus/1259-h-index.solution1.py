# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: h-index
# source_path: LeetCode-Solutions-master/Python/h-index.py
# solution_class: Solution
# submission_id: 592e52d9843740741226ee257cee7b3dcecdcb27
# seed: 3505465294

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0] * (n + 1)
        for x in citations:
            # Put all x >= n in the same bucket.
            if x >= n:
                count[n] += 1
            else:
                count[x] += 1

        h = 0
        for i in reversed(xrange(0, n + 1)):
            h += count[i]
            if h >= i:
                return i
        return h