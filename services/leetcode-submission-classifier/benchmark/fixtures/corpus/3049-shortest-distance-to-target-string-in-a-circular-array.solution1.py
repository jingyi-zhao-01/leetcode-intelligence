# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-distance-to-target-string-in-a-circular-array
# source_path: LeetCode-Solutions-master/Python/shortest-distance-to-target-string-in-a-circular-array.py
# solution_class: Solution
# submission_id: 981fd05e459a02f46eac626b0b1d0a71df6a7145
# seed: 1893750206

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def closetTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        INF = float("inf")
        result = INF
        for i, w in enumerate(words):
            if w == target:
                result = min(result, (i-startIndex)%len(words), (startIndex-i)%len(words))
        return result if result != INF else -1