# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-win-from-two-segments
# source_path: LeetCode-Solutions-master/Python/maximize-win-from-two-segments.py
# solution_class: Solution
# submission_id: 26ef85677aef1cde0850a3b64f532383d0f5557d
# seed: 205658568

# Time:  O(n)
# Space: O(n)

# two pointers, sliding window, dp

class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0]*(len(prizePositions)+1)
        result = left = 0
        for right in xrange(len(prizePositions)):
            while prizePositions[right]-prizePositions[left] > k:
                left += 1
            dp[right+1] = max(dp[right], right-left+1)
            result = max(result, dp[left]+(right-left+1))
        return result