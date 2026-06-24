# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-visited-integers
# source_path: LeetCode-Solutions-master/Python/last-visited-integers.py
# solution_class: Solution
# submission_id: ca8bc0d91b0b04bb292ee218d19e1c053a746609
# seed: 2317343615

# Time:  O(n)
# Space: O(n)

# stack

class Solution(object):
    def lastVisitedIntegers(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        PREV = "prev"
        result, stk = [], []
        i = -1
        for x in words:
            if x == PREV:
                result.append(stk[i] if i >= 0 else -1)
                i -= 1
                continue
            stk.append(int(x))
            i = len(stk)-1
        return result