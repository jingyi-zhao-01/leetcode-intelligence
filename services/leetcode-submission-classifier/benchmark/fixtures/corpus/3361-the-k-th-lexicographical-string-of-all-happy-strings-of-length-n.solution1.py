# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
# source_path: LeetCode-Solutions-master/Python/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n.py
# solution_class: Solution
# submission_id: c8bf0b7543e6d1d67ecbf1dd094fb6cfac8ad8dc
# seed: 2503983129

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        base = 2**(n-1)
        if k > 3*base:
            return ""
        result = [chr(ord('a')+(k-1)//base)]
        while base > 1:
            k -= (k-1)//base*base
            base //= 2
            result.append(('a' if result[-1] != 'a' else 'b') if (k-1)//base == 0 else
                          ('c' if result[-1] != 'c' else 'b'))
        return "".join(result)