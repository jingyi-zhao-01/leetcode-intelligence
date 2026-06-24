# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: length-of-last-word
# source_path: LeetCode-Solutions-master/Python/length-of-last-word.py
# solution_class: Solution2
# submission_id: 7bfe7ad97e368babf508644c1204f6af0d036b7c
# seed: 3429273476

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])