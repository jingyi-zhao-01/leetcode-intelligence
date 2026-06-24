# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-partitioning
# source_path: LeetCode-Solutions-master/Python/palindrome-partitioning.py
# solution_class: Solution2
# submission_id: 93afd59b3ce6697ff82df3bc09478bca4045d1f6
# seed: 1013591461

# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)

class Solution2(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.partitionRecu(result, [], s, 0)
        return result

    def partitionRecu(self, result, cur, s, i):
        if i == len(s):
            result.append(list(cur))
        else:
            for j in xrange(i, len(s)):
                if self.isPalindrome(s[i: j + 1]):
                    cur.append(s[i: j + 1])
                    self.partitionRecu(result, cur, s, j + 1)
                    cur.pop()

    def isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True