# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-consecutive-sequence
# source_path: LeetCode-Solutions-master/Python/longest-consecutive-sequence.py
# solution_class: Solution
# submission_id: 627b1dc397c4e14f03005b848c16959b4ed0aa2a
# seed: 940982966

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        result, lengths = 1, {key: 0 for key in num}
        for i in num:
            if lengths[i] == 0:
                lengths[i] = 1
                left, right = lengths.get(i - 1, 0), lengths.get(i + 1, 0)
                length = 1 + left + right
                result, lengths[i - left], lengths[i + right] = max(result, length), length, length
        return result