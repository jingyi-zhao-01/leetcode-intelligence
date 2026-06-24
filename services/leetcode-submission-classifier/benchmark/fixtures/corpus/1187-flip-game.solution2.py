# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-game
# source_path: LeetCode-Solutions-master/Python/flip-game.py
# solution_class: Solution2
# submission_id: 72b9b322da1de49957fa6b9d6f9c7b6daef5c144
# seed: 153192836

# Time:  O(c * n + n) = O(n * (c+1))
# Space: O(n)

class Solution2(object):
  def generatePossibleNextMoves(self, s):
      """
      :type s: str
      :rtype: List[str]
      """
      return [s[:i] + "--" + s[i+2:] for i in xrange(len(s) - 1) if s[i:i+2] == "++"]