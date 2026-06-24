# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-binary-strings-with-cost-limit
# source_path: LeetCode-Solutions-master/Python/valid-binary-strings-with-cost-limit.py
# solution_class: Solution
# submission_id: 9520fcfdac2ece2667df2509285ec9daabb5dab3
# seed: 4029164713

# Time:  O(n * 2^n)
# Space: O(n)

# backtracking

class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        def backtracking(total):
            if len(curr) == n:
                result.append("".join(curr))
                return
            curr.append('0')
            backtracking(total)
            curr.pop()
            if (not curr or curr[-1] == '0') and total+len(curr) <= k:
                curr.append('1')
                backtracking(total+(len(curr)-1))
                curr.pop()

        result, curr = [], []
        backtracking(0)
        return result