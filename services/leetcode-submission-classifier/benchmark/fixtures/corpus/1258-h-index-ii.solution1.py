# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: h-index-ii
# source_path: LeetCode-Solutions-master/Python/h-index-ii.py
# solution_class: Solution
# submission_id: 4fb382bd0f3f9f38fd818182a5bc37bb0e1732dd
# seed: 3240471499

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left