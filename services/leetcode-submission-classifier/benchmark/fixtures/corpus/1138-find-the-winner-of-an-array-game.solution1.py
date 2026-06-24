# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-winner-of-an-array-game
# source_path: LeetCode-Solutions-master/Python/find-the-winner-of-an-array-game.py
# solution_class: Solution
# submission_id: 6bbcffef84a5cadf63e115b03e9cbc3fa9f981a8
# seed: 851420591

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        result = arr[0]
        count = 0
        for i in xrange(1, len(arr)):
            if arr[i] > result:
                result = arr[i]
                count = 0
            count += 1
            if (count == k):
                break
        return result