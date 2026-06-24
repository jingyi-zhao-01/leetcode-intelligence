# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-numbers-are-ascending-in-a-sentence
# source_path: LeetCode-Solutions-master/Python/check-if-numbers-are-ascending-in-a-sentence.py
# solution_class: Solution
# submission_id: 4dd8f5eca8bc738e1f89209100d1dfe502a09fee
# seed: 4116435834

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = curr = -1
        for i, c in enumerate(s):
            if c.isdigit():
                curr = max(curr, 0)*10+int(c)
                continue
            if prev != -1 and curr != -1 and prev >= curr:
                return False
            if curr != -1:
                prev = curr
            curr = -1            
        return curr == -1 or prev < curr