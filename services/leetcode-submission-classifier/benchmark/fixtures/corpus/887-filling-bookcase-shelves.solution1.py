# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: filling-bookcase-shelves
# source_path: LeetCode-Solutions-master/Python/filling-bookcase-shelves.py
# solution_class: Solution
# submission_id: 2e2938c0abe8fbf3f14b6d948364cb4cceb16a62
# seed: 3553553597

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        dp = [float("inf") for _ in xrange(len(books)+1)]
        dp[0] = 0
        for i in xrange(1, len(books)+1):
            max_width = shelf_width
            max_height = 0
            for j in reversed(xrange(i)):
                if max_width-books[j][0] < 0:
                    break
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j]+max_height)
        return dp[len(books)]