# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: hash-divided-string
# source_path: LeetCode-Solutions-master/Python/hash-divided-string.py
# solution_class: Solution
# submission_id: 6661c00afabbe54653bce5689a4bbb7efb28a14d
# seed: 3117954700

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = (chr(ord('a')+reduce(lambda accu, x: (accu+x)%26,  (ord(s[i+j])-ord('a') for j in xrange(k)), 0)) for i in xrange(0, len(s), k))
        return "".join(result)