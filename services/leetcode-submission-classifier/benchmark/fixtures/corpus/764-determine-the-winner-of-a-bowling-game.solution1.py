# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-the-winner-of-a-bowling-game
# source_path: LeetCode-Solutions-master/Python/determine-the-winner-of-a-bowling-game.py
# solution_class: Solution
# submission_id: 273439afee1bfc81adf77bd017cf92a76f5a9da2
# seed: 2203634938

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        k = 2
        def f(arr):
            result = cnt = 0
            for i in xrange(len(arr)):
                result += 2*arr[i] if cnt else arr[i]
                cnt += (arr[i] == 10)
                if i-k >= 0:
                    cnt -= (arr[i-k] == 10)
            return result

        a, b = f(player1), f(player2)
        return 1 if a > b else 2 if a < b else 0