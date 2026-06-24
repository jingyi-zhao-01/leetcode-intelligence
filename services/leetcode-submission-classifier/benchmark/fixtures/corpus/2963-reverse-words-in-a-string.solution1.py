# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-words-in-a-string
# source_path: LeetCode-Solutions-master/Python/reverse-words-in-a-string.py
# solution_class: Solution
# submission_id: 870567ac9e0fefa8bc5aaf8a8fcb0d83c5ef338d
# seed: 3091987742

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))