# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: can-make-palindrome-from-substring
# source_path: LeetCode-Solutions-master/Python/can-make-palindrome-from-substring.py
# solution_class: Solution
# submission_id: d3de6ef6db55625b0c1d769772b9c03c6c5a016d
# seed: 2558355232

# Time:  O(m + n), m is the number of queries, n is the length of s
# Space: O(n)

import itertools

class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        CHARSET_SIZE = 26
        curr, count = [0]*CHARSET_SIZE, [[0]*CHARSET_SIZE]
        for c in s:
            curr[ord(c)-ord('a')] += 1
            count.append(curr[:])
        return [sum((b-a)%2 for a, b in itertools.izip(count[left], count[right+1]))//2 <= k
                for left, right, k in queries]