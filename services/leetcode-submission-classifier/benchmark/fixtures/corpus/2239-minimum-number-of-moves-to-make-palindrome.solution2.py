# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-moves-to-make-palindrome
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-moves-to-make-palindrome.py
# solution_class: Solution2
# submission_id: 4f3cdd3cef76fe96131ac21811a4c83b0c2953f8
# seed: 2898967045

# Time:  O(nlogn)
# Space: O(n)

class BIT(object):  # 0-indexed
    def __init__(self, n):
        self.__bit = [0]*(n+1)

    def add(self, i, val):
        i += 1
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret


# greedy, bit, fenwick tree

class Solution2(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        result = 0
        while s:
            i = s.index(s[-1])
            if i == len(s)-1:
                result += i//2
            else:
                result += i
                s.pop(i)
            s.pop()
        return result