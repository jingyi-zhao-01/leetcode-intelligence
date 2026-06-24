# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-adjacent-almost-equal-characters
# source_path: LeetCode-Solutions-master/Python/remove-adjacent-almost-equal-characters.py
# solution_class: Solution
# submission_id: 9d555d350c420fe72c28659f74b424689a2346ea
# seed: 345533094

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = 0
        for i in xrange(len(word)-1):
            if (i+1)+result >= len(word):
                break
            if abs(ord(word[(i+1)+result])-ord(word[i+result])) <= 1:
                result += 1
        return result