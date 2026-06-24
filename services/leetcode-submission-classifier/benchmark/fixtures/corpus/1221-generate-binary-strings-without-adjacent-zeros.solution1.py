# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-binary-strings-without-adjacent-zeros
# source_path: LeetCode-Solutions-master/Python/generate-binary-strings-without-adjacent-zeros.py
# solution_class: Solution
# submission_id: 72270ad6e872f5a899c88913f18cdfd9891d4a61
# seed: 2605634303

# Time:  O(n * 2^n)
# Space: O(n)

# backtracking

class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtracking(i):
            if i == n:
                result.append("".join(curr))
                return
            if not curr or curr[-1] == '1':
                curr.append('0')
                backtracking(i+1)
                curr.pop()
            curr.append('1')
            backtracking(i+1)
            curr.pop()

        result, curr = [], []
        backtracking(0)
        return result