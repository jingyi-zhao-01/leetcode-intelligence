# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shifting-letters
# source_path: LeetCode-Solutions-master/Python/shifting-letters.py
# solution_class: Solution
# submission_id: 178e5b677dd7c5ff7442b43d008ee0580ecb29b6
# seed: 437379459

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        result = []
        times = sum(shifts) % 26
        for i, c in enumerate(S):
            index = ord(c) - ord('a')
            result.append(chr(ord('a') + (index+times) % 26))
            times = (times-shifts[i]) % 26
        return "".join(result)