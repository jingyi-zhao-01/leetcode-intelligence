# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: length-of-last-word
# source_path: LeetCode-Solutions-master/Python/length-of-last-word.py
# solution_class: Solution
# submission_id: 578f01a7d00fbc0658c4d8821f680ccab9139bda
# seed: 2335510851

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length