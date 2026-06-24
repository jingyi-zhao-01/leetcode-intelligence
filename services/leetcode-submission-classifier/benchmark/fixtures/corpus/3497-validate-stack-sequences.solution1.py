# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: validate-stack-sequences
# source_path: LeetCode-Solutions-master/Python/validate-stack-sequences.py
# solution_class: Solution
# submission_id: 0782ef007b12ff6ccaa8c0c178a06ff6caa4bd68
# seed: 2436961446

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = 0
        s = []
        for v in pushed:
            s.append(v)
            while s and i < len(popped) and s[-1] == popped[i]:
                s.pop()
                i += 1
        return i == len(popped)