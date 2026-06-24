# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-reverse
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-reverse.py
# solution_class: Solution3
# submission_id: ddcb038fec24614fae984c923dc161a2a256fac1
# seed: 2277213152

# Time:  O(nlogn)
# Space: O(n)

# rolling hash, binary search

class Solution3(object):
    def lexSmallest(self, s):
        """
        :type s: str
        :rtype: str
        """
        return min(min(s[:k][::-1]+s[k:], s[:-k]+s[-k:][::-1]) for k in xrange(1, len(s)+1))